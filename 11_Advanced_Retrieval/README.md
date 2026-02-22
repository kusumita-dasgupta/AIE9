<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">Session 11: Advanced Retrieval with LangChain</h1>
| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Advanced Retrievers](https://github.com/AI-Maker-Space/AIE9/blob/main/00_Docs/Session_Sheets/11_Advanced_Retrievers.md) |[Recording!](https://us02web.zoom.us/rec/share/xx5RHfpbWH5qk9MRnT7ez0P6z0g4rOXGX1yv2DtPNra9r5W-5f48_hkSikNmd2-X.BJMGKIvavFPg7M9i) <br> passcode: `?aLJ0gG^`| [Session 11 Slides](https://www.canva.com/design/DAG-EL_vKlU/CRLxgnhmeWO4nU5hqAiA_g/edit?utm_content=DAG-EL_vKlU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here!| [Session 11 Assignment: Adv. Retrievers](https://forms.gle/vWLCMYWL8vEgGB54A) | [Feedback 2/17](https://forms.gle/L6itmWo7n2nkLQUu7) |

### Prerequisites

Create a `.env` file in this directory with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   COHERE_API_KEY=your_cohere_api_key_here
   ```
2. Run `uv sync` to install dependencies.

# Build 🏗️

Run the notebook and complete the following:

- 🤝 Breakout Room Part #1
  - Task 1: Getting Dependencies!
  - Task 2: Data Collection and Preparation
  - Task 3: Setting Up QDrant!
  - Tasks 4-10: Retrieval Strategies
    - Naive RAG Chain
    - Best-Matching 25 (BM25)
    - Contextual Compression (Using Reranking)
    - Multi-Query
    - Parent Document
    - Ensemble
    - Semantic Chunking
- 🤝 Breakout Room Part #2
  - Activity: Evaluate with Ragas


<details>
<summary>🚧 Advanced Build 🚧 (OPTIONAL - <i>open this section for the requirements</i>)</summary>

>NOTE: This can be done in place of the Main Assignment

Implement [RAG-Fusion](https://arxiv.org/pdf/2402.03367) using the LangChain ecosystem.

When submitting, provide:
- Your Loom video link demonstrating the semantic chunking implementation
- The GitHub URL to your completed Advanced Build

Have fun!

Advanced Build Details :
Implemented Evol-Instruct style synthetic dataset generation using a LangGraph pipeline instead of Ragas KG generation. The graph generates evolved questions (simple, multi-context, reasoning), attaches reference contexts from the corpus, and produces ground-truth answers constrained to those contexts. Final outputs include: (1) list of evolved questions with IDs and evolution types, (2) list of answers keyed by question ID, and (3) list of reference contexts keyed by question ID. The system takes a list of LangChain Documents as input and emits deterministic structured JSON outputs for grading and downstream evaluation.

New files added :
  i. evolved_questions.json
  ii. answers.json
  iii. contexts.json

</details>

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
2. **IMPORTANT:** Start Cursor from the `11_Advanced_Retrieval` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Answer Questions 1 - 3 using the `##### Answer:` markdown cell below them in `Advanced_Retrieval_with_LangChain_Assignment.ipynb`
4. Complete Activity #1 in `Advanced_Retrieval_with_LangChain_Assignment.ipynb`
5. Add, commit and push your modified notebooks to your GitHub repository.

When submitting your homework, provide:
- Your Loom video link
- The GitHub URL to the `11_Advanced_Retrieval` folder on your assignment branch
