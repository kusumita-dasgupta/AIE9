from typing import Literal

from pydantic import BaseModel, Field
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition

from app.state import MessagesState
from app.models import get_model
from app.tools import get_tool_belt


tools = get_tool_belt()
tool_node = ToolNode(tools)
model = get_model().bind_tools(tools)


class VibeCheckResult(BaseModel):
    vibe: Literal["clear", "needs_improvement"] = Field(
        description="Whether the assistant response has a clear, professional, useful vibe or needs improvement."
    )
    reason: str = Field(
        description="Short explanation for the evaluation decision."
    )


judge_model = get_model()


def agent_node(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": [response]}


def vibe_check_node(state: MessagesState):
    last_message = state["messages"][-1]

    evaluator_prompt = SystemMessage(
        content=(
            "You are a strict evaluator of assistant responses. "
            "Check whether the assistant's latest response has a clear, professional, concise, and useful vibe. "
            "Mark 'clear' if the answer is direct, grounded, and easy to understand. "
            "Mark 'needs_improvement' if it is vague, rambling, confusing, or unhelpful."
        )
    )

    structured_judge = judge_model.with_structured_output(VibeCheckResult)
    result = structured_judge.invoke([evaluator_prompt, last_message])

    return {
        "vibe_result": result.vibe,
        "vibe_reason": result.reason
    }


def route_after_vibe_check(state: dict):
    message_count = len(state["messages"])
    vibe_result = state.get("vibe_result", "clear")

    # loop guard to avoid infinite retries
    if message_count >= 8:
        return END

    if vibe_result == "needs_improvement":
        return "rewrite_node"

    return END


def rewrite_node(state: MessagesState):
    rewrite_prompt = SystemMessage(
        content=(
            "Rewrite your previous answer so it is clearer, more direct, more professional, "
            "and more useful. Keep it concise but complete."
        )
    )

    response = model.invoke([rewrite_prompt] + state["messages"])
    return {"messages": [response]}


graph_builder = StateGraph(MessagesState)

graph_builder.add_node("agent", agent_node)
graph_builder.add_node("tools", tool_node)
graph_builder.add_node("vibe_check", vibe_check_node)
graph_builder.add_node("rewrite_node", rewrite_node)

graph_builder.set_entry_point("agent")

graph_builder.add_conditional_edges(
    "agent",
    tools_condition,
    {
        "tools": "tools",
        "__end__": "vibe_check",
    },
)

graph_builder.add_edge("tools", "agent")

graph_builder.add_conditional_edges(
    "vibe_check",
    route_after_vibe_check,
    {
        "rewrite_node": "rewrite_node",
        END: END,
    },
)

graph_builder.add_edge("rewrite_node", "vibe_check")

graph = graph_builder.compile()