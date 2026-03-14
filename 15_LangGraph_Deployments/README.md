<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">Session 15: Build & Serve Agentic Graphs with LangGraph</h1>

| 📰 Session Sheet                                             | ⏺️ Recording                           | 🖼️ Slides                                  | 👨‍💻 Repo    | 📝 Homework                                      | 📁 Feedback                                          |
| ------------------------------------------------------------ | -------------------------------------- | ------------------------------------------- | ------------- | ------------------------------------------------ | ---------------------------------------------------- |
| [Agent Servers](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Session_Sheets/15_Agent_Servers) |[Recording!](https://us02web.zoom.us/rec/share/lORjByDju6fv4TdE3r93dorY3aNgmSKL_Qk_cX_AMcCQ6cNfSW77unaA1LMVV60.OcI8uEnfVmRAgjSn) <br> passcode: `Dc@&pv1T`| [Session 15 Slides](https://www.canva.com/design/DAG-EJqkRaM/FR3WG_yMA5_BqbWpQlHR9g/edit?utm_content=DAG-EJqkRaM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 15 Assignment: Agent Servers](https://forms.gle/Vb3HNDsyVPQ1jqKX7) | [Feedback 3/3](https://forms.gle/kYmhbVUEMog16mKv8) |

### Prerequisites

Before starting, ensure you have the following:

- **Python 3.11+** installed
- An **OpenAI API Key**
- A **Tavily API Key**
- (Optional) **LangSmith** credentials for tracing

Create a `.env` file in this directory with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```
2. Run `uv sync` to install dependencies.

# Build 🏗️

Run the repository and complete the following:

- 🤝 Breakout Room Part #1 — Building and serving your LangGraph Agent Graph
  - Task 1: Getting Dependencies & Environment
    - Configure `.env` (OpenAI, Tavily, optional LangSmith)
  - Task 2: Serve the Graph Locally
    - `uv run langgraph dev` (API on http://localhost:2024)
  - Task 3: Call the API from a different terminal
    - `uv run test_served_graph.py` (sync SDK example)
  - Task 4: Explore assistants (from `langgraph.json`)
    - `agent` → `simple_agent` (tool-using agent)
    - `agent_helpful` → `agent_with_helpfulness` (separate helpfulness node)

- 🤝 Breakout Room Part #2 — Using LangSmith Studio to visualize the graph
  - Task 1: Open Studio while the server is running
    - https://smith.langchain.com/studio?baseUrl=http://localhost:2024
  - Task 2: Visualize & Stream
    - Start a run and observe node-by-node updates
  - Task 3: Compare Flows
    - Contrast `agent` vs `agent_helpful` (tool calls vs helpfulness decision)

<details>
<summary>🚧 Advanced Build 🚧 (OPTIONAL - <i>open this section for the requirements</i>)</summary>

>NOTE: This can be done in place of the Main Assignment

- Create and deploy a locally hosted MCP server with FastMCP.
- Extend your tools in `tools.py` to allow your LangGraph to consume the MCP Server.

When submitting, provide:
- Your Loom video link demonstrating the MCP server integration
- The GitHub URL to your completed Advanced Build

Have fun!
</details>

### Questions & Activities

#### Question 1:
What is the key architectural difference between the `simple_agent` and `agent_with_helpfulness` graphs? Specifically, explain how the helpfulness evaluation loop works and what mechanisms are in place to prevent it from running indefinitely.

##### Answer:
The simple_agent graph is a standard tool-calling LangGraph agent loop. It has an agent node that receives the user message, decides whether it can answer directly or needs to call a tool, and then either ends the run or routes execution to a ToolNode. If a tool is called, the tool result is added back into the state and control returns to the agent node so the model can continue reasoning with the new information. Architecturally, this graph focuses only on producing an answer, using conditional routing through tools_condition to decide whether to continue the loop or terminate.

The agent_with_helpfulness graph adds an additional evaluation stage after the agent produces a response. Instead of ending immediately after the agent answer, the graph routes the output to a separate helpfulness evaluation node. That node uses a model with structured output to judge whether the answer is helpful, typically returning a constrained result such as “yes” or “no.” If the answer is judged helpful, the graph terminates. If it is judged unhelpful, the graph loops back to the agent node so the agent can try again and generate an improved response. This creates an evaluate-and-retry pattern rather than a single-pass generation flow.

The helpfulness loop is prevented from running forever by an explicit loop guard. The graph checks the state, typically by looking at message count or retry count, and stops retrying once a defined limit is reached. This ensures the agent does not enter an infinite evaluation cycle that wastes tokens, time, or cost. In other words, the simple_agent is a basic tool-using agent, while agent_with_helpfulness is a self-correcting agent that adds a bounded model-as-judge feedback loop on top of the normal tool-calling architecture.



#### Question 2:
What is the role of `langgraph.json` in the LangGraph Deployments? Describe each of its key fields and how the platform uses this file to discover and serve your graphs.

##### Answer:
langgraph.json is the deployment manifest for a LangGraph application. Its role is to tell the LangGraph runtime which graphs exist, where they are defined in the codebase, and which assistants should be exposed when the application is served. Without this file, the deployment platform would not know what graph objects to load or how to present them as runnable assistants in local development, Studio, or production deployment.

The most important field is graphs. This is a mapping between a graph identifier and the Python import path for the compiled graph object. For example, a value such as "simple_agent": "./app/graphs/simple_agent.py:graph" tells the platform to load the object named graph from that file and register it under the graph ID simple_agent. This is how LangGraph discovers the executable graph definitions in the project.

The second key field is assistants. This is a list of assistant configurations that define the user-facing runnable endpoints built on top of those graphs. Each assistant entry typically includes fields such as assistant_id, name, graph_id, and description. assistant_id is the unique identifier used when calling the assistant through the SDK or API. name is the human-readable label shown in interfaces such as Studio. graph_id links that assistant back to one of the graph definitions in the graphs section. description provides a short explanation of what that assistant does. This design allows one graph to potentially support multiple assistants with different identities or configurations.

When the platform starts, it reads langgraph.json, imports the graph objects listed under graphs, and then registers the assistants listed under assistants so they can be served through the local API, visualized in LangGraph Studio, and deployed through LangSmith. In practice, langgraph.json acts as the contract between your codebase and the deployment platform: it is the file that makes your graphs discoverable, selectable, and runnable.



#### Activity #1:
Create your own agent graph! Build a new graph in `app/graphs/` with a custom evaluation node (e.g., a vibe checker, a fact verifier, a summarizer — get creative!). Register it in `langgraph.json`, serve it with `uv run langgraph dev`

##### Answer:
The new graph I built is vibe_checker_agent, created in app/graphs/vibe_checker_agent.py. It follows the normal LangGraph tool-calling pattern but adds a custom evaluation node called vibe_check_node after the main agent response. This node uses structured output to classify the answer as either clear or needs_improvement based on whether the response is direct, professional, concise, and useful. If the answer passes the vibe check, the graph ends. If it fails, the graph routes to a rewrite_node, which asks the model to rewrite the answer more clearly and then sends it back for another vibe check. I also added a loop guard based on message count so the graph cannot retry indefinitely. After registering the graph in langgraph.json, I served it locally with uv run langgraph dev and verified it in LangGraph Studio.


# Ship 🚢

- The completed notebook.
- 5min. Loom Video

# Share 🚀

- Walk through your notebook and explain what you've completed in the Loom video
- Make a social media post about your final application and tag @AIMakerspace
- Share 3 lessons learned
- Share 3 lessons not learned

# Submitting Your Homework

### Main Homework Assignment

Follow these steps to prepare and submit your homework:

1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
    - _(You should have completed this process already.)_ For your initial repo setup, see [Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `15_LangGraph_Platform` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Answer Questions 1 - 2 using the `##### Answer:` markdown cell below them in the README
4. Complete Activity #1 in the README
5. Add, commit and push your modified files to your GitHub repository.

When submitting your homework, provide:
- Your Loom video link
- The GitHub URL to the `15_LangGraph_Platform` folder on your assignment branch
