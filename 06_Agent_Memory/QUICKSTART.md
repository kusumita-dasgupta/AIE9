# QUICKSTART: Multi-Agent Wellness System with Shared Memory (LangGraph)

This project implements a multi-agent wellness assistant using LangGraph and the CoALA memory framework, where specialist agents collaborate through a shared memory store.

## Agents

- **Router Agent** – routes user queries to the right specialist
- **Exercise Agent** – fitness and physical activity
- **Nutrition Agent** – diet and meal guidance
- **Sleep Agent** – sleep quality and recovery

Each agent has its own episodic + procedural memory, while sharing user profile and wellness knowledge.

---

## 1. Architecture Overview

### High-Level Flow

```
User Query
   │
   ▼
┌───────────────────────┐
│     Router Agent      │  (GPT-4o)
│  Structured Output    │
│   RouterDecision      │
└───────────┬───────────┘
            │
   ┌────────┼─────────┐
   ▼        ▼         ▼
Exercise  Nutrition   Sleep
 Agent      Agent      Agent
 (GPT-4o-mini, domain prompts)
   │        │         │
   └────────┼─────────┘
            ▼
     Unified Response
```

### Namespace Strategy (Critical for Memory)

**Shared Memory** (all agents can read)

| Namespace | Purpose |
|-----------|---------|
| `(user_id, "profile")` | Long-term: user goals, conditions, preferences |
| `("wellness", "knowledge")` | Semantic: shared wellness knowledge base |

**Per-Agent Memory** (isolated, but discoverable)

| Namespace | Type |
|-----------|------|
| `("exercise_agent", "instructions")` | Procedural memory |
| `("exercise_agent", "episodes")` | Episodic memory |
| `("nutrition_agent", "instructions")` | Procedural memory |
| `("nutrition_agent", "episodes")` | Episodic memory |
| `("sleep_agent", "instructions")` | Procedural memory |
| `("sleep_agent", "episodes")` | Episodic memory |

**Cross-Agent Learning**

Specialists search each other's episodic memory.  
*Example:* Nutrition Agent learns from Exercise Agent's successful injury-aware advice.

---

## 2. Memory Types Used

| Memory Type | Implementation | Purpose |
|-------------|----------------|---------|
| Short-term | MemorySaver + `thread_id` | Conversation context |
| Long-term | Store + namespaces | User profile across sessions |
| Semantic | Embeddings + `store.search()` | Meaning-based knowledge retrieval |
| Episodic | Stored examples | Learn from past successes |
| Procedural | Self-updating instructions | Improve advice style |

---

## 3. How to Run the Multi-Agent System

### Prerequisites

**Create `.env`:**

```env
OPENAI_API_KEY=sk-...
LANGCHAIN_API_KEY=ls-...
LANGCHAIN_TRACING_V2=true
```

**Install deps:**

```bash
uv sync
```

### Start LangGraph Studio

From the `06_Agent_Memory` directory:

```bash
uv run langgraph dev
```

**Access:**

- **Studio UI:** http://localhost:2024  
- **API Docs:** http://localhost:2024/docs  

### Run the Notebook

Open and run:

```
Agent_Memory_Assignment.ipynb
```

**Key cells to execute:**

1. Router Agent (RouterDecision)
2. Specialist agents (Exercise / Nutrition / Sleep)
3. Shared + per-agent memory setup
4. Memory dashboard

---

## 4. Memory Dashboard

The dashboard is text-based (not UI) and generated via an agent.

### What It Shows

- User profile (shared long-term memory)
- Procedural instruction versions per agent
- Episodic memory counts per agent
- Semantic + episodic memory search results

### Example: Weekly Wellness Summary

**User Input**

> Give me a summary of my wellness this week

**Agent Output**

- Sleep quality improved from 5 → 7
- Energy dipped mid-week
- Mood improved on days with exercise

*Based on past successful interactions:*
- Low-impact workouts helped on injury days
- Earlier bedtime reduced fatigue

*Suggested focus:*
- Consistent sleep schedule
- Light exercise on low-energy days
- Protein-rich breakfast

### Example: Cross-Agent Learning

**User**

> I want to lose weight but my knee hurts

**System Behavior**

1. **Router** → Exercise Agent  
2. **Exercise Agent:**
   - Reads user profile
   - Pulls episodic memory from Exercise + Nutrition agents
   - Generates injury-aware + diet-aligned advice

---

## 5. Why This Architecture Works

- **Scales cleanly** → add more specialist agents
- **Memory isolation** → avoids agent interference
- **Shared truth** → user profile & knowledge stay consistent
- **Learning loop** → episodic + procedural memory improve responses over time

---

## 6. Files of Interest

| File | Purpose |
|------|---------|
| `Agent_Memory_Assignment.ipynb` | Core implementation |
| `QUICKSTART.md` | This guide |
| `.env` | API keys |
| `HealthWellnessGuide.txt` | Semantic KB |

7. Next Extensions (Optional)

Replace InMemoryStore with Postgres

Add TTL for episodic memory

Add importance scoring for memories

Add Streamlit dashboard

Built with LangGraph + CoALA memory patterns
Inspired by AI Makerspace – AIE9