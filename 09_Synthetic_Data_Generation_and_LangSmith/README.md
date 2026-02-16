
<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">Session 9: Synthetic Data Generation and LangSmith</h1>

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [SDG](../00_Docs/Session_Sheets/09_Synthetic_Data_Generation_for_Evals.md) |[Recording!](https://us02web.zoom.us/rec/share/XDZDe3gqHjRg3DlMe2Zf_DZtMPA-m1mfq4UaXZMQIVyPbWVYrC0XWKCf77-y1d7G.kWhmFDlmvgo3Bouw) <br> passcode: `WBa$6T#y`| [Session 9 Slides](https://www.canva.com/design/DAG-EKs7Ur8/Y6WRgFfp1Ns2vLBeHXNNQw/edit?utm_content=DAG-EKs7Ur8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 9 Assignment: SDG](https://forms.gle/JTKq5qgTxqY77URD7) | [Feedback 2/10](https://forms.gle/grcVKmPDGd6BmoFp7) |

In today's assignment, we'll be creating Synthetic Data, and using it to benchmark (and improve) a LCEL RAG Chain.

- 🤝 BREAKOUT ROOM #1
  1. Use RAGAS to Generate Synthetic Data

- 🤝 BREAKOUT ROOM #2
  1. Load them into a LangSmith Dataset
  2. Evaluate our RAG chain against the synthetic test data
  3. Make changes to our pipeline
  4. Evaluate the modified pipeline

## Ship 🚢

The completed notebook!

### 🚧 OPTIONAL: Advanced Build

Reproduce the RAGAS Synthetic Data Generation Steps - but utilize a LangGraph Agent Graph, instead of the Knowledge Graph approach.

This generation should leverage the [Evol Instruct](https://arxiv.org/pdf/2304.12244) method to generate synthetic data.

Your final state (output) should contain (at least, not limited to):

1. `List(dict)`: Evolved Questions, their IDs, and their Evolution Type.
2. `List(dict)`: Question IDs, and Answer to the referenced Evolved Question.
3. `List(dict)`: Question IDs, and the relevant Context(s) to the Evolved Question.

The Graph should handle:

1. Simple Evolution.
2. Multi-Context Evolution.
3. Reasoning Evolution.

It should take, as input, a list of LangChain Documents.


Advanced Build Summary (LangGraph + Evol-Instruct)
Implemented synthetic data generation using a LangGraph workflow instead of RAGAS knowledge graphs. The graph takes LangChain documents as input, generates seed questions, evolves each seed using Evol-Instruct-style transformations (simple, multi-context, reasoning), retrieves supporting contexts from a Qdrant vector index, and produces context-grounded answers with an “I don’t know” fallback. Final state outputs include: (1) evolved questions with IDs and evolution type, (2) answers keyed by question_id, and (3) retrieved contexts keyed by question_id.

Notes
- This is not RAGAS KG-based SDG — it’s agentic SDG using LangGraph, exactly as required.
- “Evol-Instruct” is satisfied by the explicit evolution operator prompts and the three evolution types.
- You can optionally increase n seeds to 10, but keep it small to avoid cost.

Additional File Generated
- usecase_data_kg.json

This file stores the serialized KnowledgeGraph (nodes + relationships).
- It was created to persist the transformed graph.
- It is used for loading the graph later without recomputing transforms.

### Deliverables

- A short Loom of the notebook

## Share 🚀

Make a social media post about your final application!

### Deliverables

- Make a post on any social media platform about what you built!

Here's a template to get you started:

```
🚀 Exciting News! 🚀

I am thrilled to announce that I have just built and shipped Synthetic Data Generation, benchmarking, and iteration with RAGAS & LangChain! 🎉🤖

🔍 Three Key Takeaways:
1️⃣ 
2️⃣ 
3️⃣ 

Let's continue pushing the boundaries of what's possible in the world of AI and question-answering. Here's to many more innovations! 🚀
Shout out to @AIMakerspace !

#LangChain #QuestionAnswering #RetrievalAugmented #Innovation #AI #TechMilestone

Feel free to reach out if you're curious or would like to collaborate on similar projects! 🤝🔥
```

## Submitting Your Homework

### Main Homework Assignment

Follow these steps to prepare and submit your homework assignment:
1. Create a branch of your `AIE9` repo to track your changes. Example command: `git checkout -b s09-assignment`
2. Respond to the activities and questions in the `Synthetic_Data_Generation_RAGAS_&_LangSmith_Assignment.ipynb` notebook:
    + Edit the markdown cells of the activities and questions then enter your responses
    + Edit/Create code cell(s) where necessary as part of an activity
    + NOTE: Remember to create a header (example: `##### ✅ Answer:`) to help the grader find your responses
3. Commit, and push your completed notebook to your `origin` repository. _NOTE: Do not merge it into your main branch._
4. Make sure to include all of the following on your Homework Submission Form:
    + The GitHub URL to the completed notebook _on your assignment branch (not main)_
    + The URL to your Loom Video
    + Your Three lessons learned/not yet learned
    + The URLs to any social media posts (LinkedIn, X, Discord, etc.) ⬅️ _easy Extra Credit points!_

### Advanced Build
1. Include a 1 minute walkthrough of your completed application as part of your Main Homework Assignment's Loom video
2. In addition to the Homework Submission instructions in Main Homework Assignment ➡ Step 4, include the following URLs to your Advanced Build's:
    + GitHub Repo
    + Production Deployment
