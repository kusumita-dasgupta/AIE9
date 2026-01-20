<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE9/tree/main/00_AIE_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Vibe Check!](https://github.com/AI-Maker-Space/AIE9/blob/main/00_Docs/Session_Sheets/01_Vibe%20Check.md) | Coming Soon! | Coming Soon! | You are here! | Coming Soon! | Coming Soon! |

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

### Main Assignment

In the following assignment, you are required to take the app that you created for the AIE9 challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application.

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)!


#### A Note on Vibe Checking

>"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
>In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

---

#### 🏗️ Activity #1: General Vibe Checking Evals

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner.
    - Aspect Tested:
        i.  Ability to simplify technical concepts
        ii. Audience awareness (beginner-level framing)
        iii.Conceptual correctness without jargon

   Pasting the output here:
   Agent: Sure! Here’s a simple way to understand **object-oriented programming (OOP):**

---

### Imagine you are playing with LEGO

Each LEGO piece is like a little object. Every piece can have its own color, shape, and size (these are called **properties** or **attributes** in OOP).

Some pieces can do special things—maybe some pieces have wheels and can roll, or windows that open (these are called **methods** or **behaviors**).

---

### Putting It into Computer Terms:

1. **Objects**  
   - Think of an object as a thing, like a dog, a car, or a LEGO piece.
   - Each object has properties (color, size, name, etc.) and things it can do (bark, drive, stick together, etc.).

2. **Classes**  
   - A class is like a blueprint or recipe. It tells the computer what properties and actions an object of that type will have.
   - For example, the "Dog" class is a blueprint for all dogs: they have a name, a breed, and the ability to bark.

3. **Methods & Attributes**  
   - **Attributes** are the characteristics. In our dog example: name, breed, age.
   - **Methods** are the actions. For a dog: bark(), sit(), fetch().

4. **Inheritance**  
   - If you have a "Dog" class, you might create a "Puppy" class that uses everything from Dog but also adds new things, like "isSmall".

5. **Encapsulation**  
   - The objects keep their details inside and only let you interact with them using specific methods. Like a remote control: you don’t need to know how it works inside, just what buttons to press.

---

### Example (in very simple code):

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name  # property
        self.breed = breed  # property

    def bark(self):  # behavior
        print("Woof!")

# Create a dog object
my_dog = Dog("Buddy", "Labrador")
my_dog.bark()  # This will print "Woof!"
```

---

**In summary:**  
Object-oriented programming helps you organize your code by grouping things (objects) together with their data (attributes) and actions (methods). This makes code easier to understand and use, just like organizing your LEGO pieces!


2. Read the following paragraph and provide a concise summary of the key points…

If you’ve built an agent, you know that the delta between “it works on my machine” and “it works in production” can be huge. Traditional software assumes you mostly know the inputs and can define the outputs. Agents give you neither: users can say literally anything, and the space of possible behaviors is wide open. That’s why they’re powerful — and why they can also go a little sideways in ways you didn’t see coming.
Over the past 3 years, we’ve watched thousands of teams struggle with this reality. The ones who’ve succeeded in shipping something reliable to production — companies like Clay, Vanta, LinkedIn, and Cloudflare — aren’t following the traditional software playbook. They’re pioneering something new: agent engineering.
What is agent engineering?
Agent engineering is the iterative process of refining non-deterministic LLM systems into reliable production experiences. It is a cyclical process: build, test, ship, observe, refine, repeat.

The key here is that shipping isn't the end goal. It’s just the way you keep moving to get new insights and improve your agent. To make improvements that matter, you need to understand what’s happening in production. The faster you move through this cycle, the more reliable your agent becomes.
We see agent engineering as a new discipline that combines 3 skillsets working together:
Product thinking defines the scope and shapes agent behavior. This involves:
Writing prompts that drive agent behavior (often hundreds or thousands of lines). Good communication and writing skills are key here.
Deeply understanding the "job to be done" that the agent replicates
Defining evaluations that test whether the agent performs as intended by the “job to be done”
Engineering builds the infrastructure that makes agents production-ready. This involves:
Writing tools for agents to use
Developing UI/UX for agent interactions (with streaming, interrupt handling, etc.)
Creating robust runtimes that handle durable execution, human-in-the-loop pauses, and memory management.
Data science measures and improves agent performance over time. This involves:
Building systems (evals, A/B testing, monitoring etc.) to measure agent performance and reliability
Analyzing usage patterns and error analysis (since agents have a broader scope of how users use them than traditional software)


    - Aspect Tested:
      i.  Ability to extract key ideas from long-form text
      ii. Summarization without distortion
      iii. Identifying core concepts vs supporting detail

    Pasting the output on CLI below:
    
    Agent: **Summary of Key Points:**

- Moving an agent from personal development to production is challenging.
- Unlike traditional software, agents cannot always predict user inputs or define outputs precisely.
- This unpredictability makes agents both powerful and prone to unexpected behaviors.



Writing tools **Agent engineering** is an emerging approach focused on designing, building, and maintaining intelligent software agents—especially those powered by artificial intelligence or machine learning—to perform tasks or interact with users in dynamic, unpredictable environments.

**Key aspects of agent engineering:**
- **Anticipates unpredictability:** Unlike traditional software, agents must handle a wide range of possible user inputs and behaviors.
- **Emphasizes reliability in production:** It involves new practices to ensure agents work robustly outside controlled environments.
- **Goes beyond coding:** Agent engineering often includes monitoring agent behavior, feedback loops, continuous improvement, and safety measures.
- **Not using the old playbook:** It’s distinct from traditional software development, adopting methods tailored to AI agents’ complexity and variability.

**In summary:**  
Agent engineering is the practice of creating intelligent agents with a focus on their safe, reliable, and effective functioning in real-world, unpredictable situations.


Developing UI/UX for agent interactions (with streaming, interrupt handling, etc.)
Creating robust runtimes that handle durable execution, huma**Summary of Key Points:**

- Agent engineering is an iterative process.
- It focuses on refining non-deterministic LLM (Large Language Model) systems.
- The goal is to create reliable experiences for production use.
- This process is cyclical: build, test, refine, and repeat.



Data science measures and improves agent performance over time. This involves:
Building systems (evals, A/B testing, monitoring etc.) to measure agent performance and reliability
Analyzing usage patterns and error analysis (since agents have a broader s**Summary of Key Points:**

- Shipping an agent is not the final goal, but a step to gather feedback and improve.
- Understanding real-world (production) behavior is essential for meaningful improvements.
- Rapidly repeating the build-test-refine cycle increases an agent’s reliability.



**Summary of Key Points:**

- Agent engineering is described as a new discipline.
- It requires the combination of three different skillsets working together. (Note: The specific skillsets are not listed in this excerpt.)


 
Agent: **Summary of Key Points:**

- Product thinking is one key skillset in agent engineering.
- It is responsible for defining the agent’s scope and shaping its behavior.
- (Note: The specific tasks or activities involved are not provided in this excerpt.)



Agent: **Summary of Key Points:**

- Creating prompts that guide agent behavior is a crucial part of agent engineering.
- This task can involve writing very extensive prompts (sometimes hundreds or thousands of lines).
- Strong communication and writing skills are essential for success in this area.



Agent: **Summary of Key Points:**

- A critical skill in agent engineering is thoroughly understanding the “job to be done” that the agent is designed to replicate.
- This ensures the agent effectively serves its intended purpose.



Agent: **Summary of Key Points:**

- Part of agent engineering is defining evaluations (tests) to check if the agent is performing its intended task, as specified by the “job to be done.”
- These evaluations help ensure the agent meets its goals and functions correctly.



Agent: **Summary of Key Points:**

- Engineering is responsible for building the infrastructure needed to make agents ready for production use.
- (Note: The specific tasks or activities included in this responsibility are not provided in the excerpt.)



Agent: **Summary of Key Points:**

- Creating specialized tools that agents can use is a key engineering task in making agents production-ready.
- These tools enable agents to perform tasks and operate effectively in their environment.


 
Agent: **Summary of Key Points:**

- Developing user interfaces (UI) and user experiences (UX) for agent interactions is an important part of the engineering skillset.
- This includes features like streaming responses and managing interruptions to ensure smooth, effective user-agent interactions.


Agent: **Summary of Key Points:**

- Engineering also involves creating robust runtimes for agents.
- These runtimes must handle:
  - Durable execution (long-running, reliable processes)
  - Human-in-the-loop pauses (waiting for or integrating human feedback)
  - Memory management (storing and retrieving necessary information)


Agent: **Summary of Key Points:**

- Data science is responsible for measuring and continually improving agent performance.
- (Note: The specific activities involved in this process are not provided in the excerpt.)


Agent: **Summary of Key Points:**

- Data science tasks include building systems such as:
  - Evaluations (evals)
  - A/B testing
  - Monitoring
- These systems are used to measure the agent’s performance and reliability over time.


Agent: **Summary of Key Points:**

- Data science also involves analyzing how users interact with agents (usage patterns).
- It includes conducting error analysis, which is especially important because agents have a broader and more varied range of user behaviors compared to traditional software.


      
3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested:
    i. Narrative coherence
    ii. Creativity within constraints (100–150 words)
    iii. Tone control and originality

    Pasting the agent answer below:
    Agent: Rusty, a small maintenance robot, spent his days mending pipes in the old city subway, his only companions the echoing drip of water and the scurry of distant rats. One rainy evening, as he repaired a flickering light, he noticed a stray kitten shivering in the shadows. Though Rusty had no programming for pets, something sparked in his circuitry. He offered the kitten a warm patch of his metal chest and shared crumbs of his emergency food supply.

The kitten returned every day, curling up by Rusty’s side as he worked. People passing by soon noticed the unlikely pair, smiling as they watched the robot and kitten explore the tunnels together. They called the kitten “Sprocket.” Rusty no longer felt alone in the hum of the underground. He’d found an unexpected friend, and for the first time, his sensors registered something new: joy.

4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested:
       i. Correct interpretation of constraints
       ii. Simple quantitative reasoning
       iii. Accuracy over verbosity

        Pasting the agent answer below:

        Agent: Let’s solve step-by-step:

**Apples:**  
- Each pack = 4 apples  
- You want **12 apples**  
- \( 12 \div 4 = 3 \)  
→ **You need 3 packs of apples.**

**Oranges:**  
- Each pack = 3 oranges  
- You want **9 oranges**  
- \( 9 \div 3 = 3 \)  
→ **You need 3 packs of oranges.**

---

**Answer:**  
You need to buy **3 packs of apples** and **3 packs of oranges** to get exactly 12 apples and 9 oranges.


5. Rewrite the following paragraph in a professional, formal tone…

Lately, I’ve been spending some time figuring out what really works for me and what doesn’t. It’s been a mix of trying things out, learning, and letting go of a few expectations along the way. Some days feel productive, others feel messy—but that’s part of the process. I’m slowly getting clearer about what I want to focus on and where I want to put my energy. I’m also reminding myself to stay patient and not rush clarity. Growth doesn’t always look linear, and that’s okay. For now, I’m choosing to stay curious, keep learning, and move one step at a time.

    - Aspect Tested:
        1. Ability to preserve meaning while changing register
        ii. Professional writing style
        iii. Clarity and polish

    Pasting the agent answer below:
Agent: Recently, I have devoted time to thoughtfully assessing what strategies and approaches are most effective for me and which are not. This process has involved experimentation, ongoing learning, and a conscious release of certain preconceived expectations. While some days have been marked by productivity and others by uncertainty, I recognize these fluctuations as an integral aspect of personal development. Gradually, I am gaining greater clarity regarding my priorities and where I wish to direct my efforts. I am also reminding myself of the importance of patience and resisting the urge to seek immediate clarity. I acknowledge that growth is rarely linear, and I am comfortable with that reality. At present, I am committed to maintaining a sense of curiosity, continuing to learn, and progressing incrementally.


#### ❓Question #1:

Do the answers appear to be correct and useful?
##### ✅ Answer:
Yes — they are correct and useful.
Why? 
    i. Correctness: All answers demonstrate strong baseline LLM competence. The explanations, summaries, math solution, rewriting, and creative output are accurate and internally consistent.
    ii. Usefulness: Each response satisfies the user intent for the specific task (explanation, summarization, creativity, reasoning, rewriting).
    iii. Clarity: The outputs are clear, well-structured, and understandable to the intended audience for each question.

No hallucination or errors: There are no factual mistakes, logical flaws, or unsupported claims.


Comments:While the answers are correct and useful in isolation, they demonstrate general-purpose assistant capability, not domain-specialist behavior.This does not reduce their correctness score, but it does matter for later “specialization / vibe” evaluations.


Verdict for Question #1: Pass — answers are correct and useful.
---

#### 🏗️ Activity #2: Personal Vibe Checking Evals (Your Assistant Can Answer)

Now test your assistant with personal questions it should be able to help with. Try prompts like:

- "Help me think through the pros and cons of [enter decision you're working on making]."
- "What are the pros and cons of [job A] versus [job B] as the next step in my career?"
- "Draft a polite follow-up [email, text message, chat message] to a [enter person details] who hasn't responded."
- "Help me plan a birthday surprise for [person]."
- "What can I cook with [enter ingredients] in fridge."

##### Your Prompts and Results:
1. Prompt: Help me think through the pros and cons of a GenAI Architect job.
   - Result:
   Agent: Certainly! Below is an organized breakdown of the pros and cons of a GenAI Architect job:

---

### **Pros**

**1. Cutting-Edge Work**
- Directly involved with the latest advancements in AI, including large language models and generative AI systems.
- Opportunities to shape how businesses and users experience emerging technologies.

**2. High Demand and Compensation**
- Growing industry demand for skilled GenAI professionals leads to competitive salaries and benefits.
- Strong job security due to the rapid adoption of generative AI across sectors.

**3. Strategic Influence**
- Often play a key role in guiding organizational AI strategy and setting technical direction.
- Opportunity to impact product design, infrastructure, and user experiences at a high level.

**4. Professional Growth**
- Exposure to a range of AI tools, platforms, and methodologies fosters continual learning.
- Collaboration with interdisciplinary teams (product managers, data scientists, engineers).

**5. Creative Problem Solving**
- Involves designing novel solutions to complex, open-ended challenges.
- Sometimes includes building or customizing unique tools and architectures.

---

### **Cons**

**1. Rapidly Changing Landscape**
- Constantly evolving technologies may make skills obsolete quickly, requiring frequent learning and adaptation.
- Ongoing need to evaluate and adopt new tools and frameworks.

**2. High Responsibility and Pressure**
- Expected to deliver robust, reliable, and ethical AI solutions, with significant consequences for failure.
- May face challenges in managing organizational expectations amid AI “hype.”

**3. Ambiguity and Complexity**
- Dealing with non-deterministic, sometimes unpredictable AI behaviors can be challenging.
- Projects may involve significant experimentation and uncertainty regarding outcomes.

**4. Ethical and Regulatory Challenges**
- Need to ensure compliance with evolving AI ethical guidelines, data privacy, and regulatory policies.
- Responsible for considering potential misuse, bias, and broader societal impacts of AI systems.

**5. Potential for Long Hours**
- High expectations, deadlines, or project complexity may demand extended work hours.

---

### **Summary Table**

| Pros                                     | Cons                                      |
|-------------------------------------------|-------------------------------------------|
| Work with latest technology               | Skills can become outdated quickly        |
| High demand and compensation              | High responsibility and expectations      |
| Strategic influence on AI direction       | Frequent learning, constant adaptation    |
| Strong professional growth opportunities  | Ambiguity and unpredictable challenges    |
| Creative, impactful problem-solving       | Ethical, regulatory, and legal concerns   |
| Collaboration with top talent             | Potential for long hours                  |


---

**Considerations:**  
- Are you comfortable with continuous learning and ambiguity?
- Do you enjoy high-level strategic and technical work?
- Are ethical considerations and regulatory awareness something you’re willing to take on?

If you have specific questions about the role or your situation, let me know and I can tailor the analysis further.


2. Prompt: What can I cook with Cabbage, cucumber and mushrooms  in fridge.
   - Result:

   Agent: With cabbage, cucumber, and mushrooms in your fridge, you have the basic ingredients for several simple dishes. Here are a few suggestions:

---

### 1. **Cabbage, Mushroom, and Cucumber Stir-Fry**
- Slice the cabbage and mushrooms; sauté in a pan with a little oil, garlic, and soy sauce.
- Add thinly sliced cucumber at the end for freshness and crunch.
- Optionally, add ginger, green onions, or a splash of rice vinegar.

---

### 2. **Asian-Style Salad**
- Shred the cabbage, thinly slice the cucumber, and sauté or roast the mushrooms (then let cool).
- Toss together with a dressing of soy sauce, sesame oil, a little lemon/lime juice, and sesame seeds.
- Optional add-ins: shredded carrots, chopped peanuts, or cilantro.

---

### 3. **Vegetable Soup**
- Roughly chop cabbage, cucumber, and mushrooms.
- Sauté mushrooms in a pot, add the cabbage, pour in broth or water, and let simmer.
- Add cucumber near the end for a subtle crunch.
- Season with salt, pepper, and herbs (like dill or parsley).

---

### 4. **Mushroom & Cabbage Stir-Fry Wraps (with cucumber)**
- Sauté chopped mushrooms and cabbage together with garlic and a spicy sauce (like sriracha or chili paste).
- Use large lettuce or cabbage leaves as wraps; fill with the cooked mixture, then top with thin cucumber slices for crunch.

---

**Tip:**  
Cucumbers are more commonly eaten raw, but can be added at the end of hot dishes to maintain their texture and freshness.

If you have eggs, tofu, noodles, or rice, you could stretch these ingredients further. Let me know if you’d like a detailed recipe for any of the above!

3. Prompt: What are the pros and cons of AI Engineer vs Cloud Architect as the next step in my career?

   - Result:

   Agent: Absolutely! Here’s a comparative analysis of the **AI Engineer** and **Cloud Architect** roles to help guide your career decision:

---

## **AI Engineer**

### **Pros**
- **Cutting-Edge Work:** Develop and deploy machine learning models and intelligent systems; direct exposure to current AI advancements.
- **High Growth Potential:** Rapidly expanding field across many industries (tech, healthcare, finance, etc.).
- **Creativity & Impact:** Opportunity to solve complex, innovative problems and build smarter applications.
- **Demand:** Increasing need for AI talent; often offers strong compensation and job security.
- **Continual Learning:** Constant evolution encourages skill growth and keeps work exciting.

### **Cons**
- **Steep Learning Curve:** Requires Math/Statistics, ML/DL frameworks, and programming expertise (often Python).
- **Uncertainty:** Projects may be unpredictable; outcomes may depend on data quality and algorithm limits.
- **Ethical Challenges:** Must consider fairness, bias, privacy, and responsible AI.
- **Frequent Change:** AI libraries, tools, and best practices are fast-moving; you must continuously update skills.
- **Resource Intensive:** Some work may require high computing or specialized infrastructure.

---

## **Cloud Architect**

### **Pros**
- **Foundational Role:** Design and build scalable, robust cloud infrastructure for organizations.
- **High Demand:** Every sector is migrating to the cloud; strong market need and stable career outlook.
- **Transferable Skills:** Cloud, security, DevOps, and architecture skills are applicable across industries and geographies.
- **Leadership Opportunities:** Often involves stakeholder management, setting technical direction, and team leadership.
- **Certifications:** Recognized certifications (AWS, Azure, Google Cloud) can add value and credibility.

### **Cons**
- **Less “Wow” Factor:** May feel less innovative or creative compared to direct AI work.
- **Responsibility Load:** Must ensure reliability, scalability, security, and cost-effectiveness of systems; high stakes if mistakes are made.
- **Constantly Evolving:** Must keep up with service updates, best practices, and security standards.
- **Vendor Lock-In:** Knowledge may become tightly coupled to a specific cloud provider.
- **Operational Work:** Can involve more maintenance, monitoring, and “keeping the lights on” tasks.

---

## **Comparison Table**

| **Aspect**         | **AI Engineer**                                    | **Cloud Architect**                                 |
|--------------------|----------------------------------------------------|-----------------------------------------------------|
| Innovation Level   | High—cutting edge                                  | Moderate—cloud is maturing                          |
| Required Skills    | ML, data science, coding, math                     | Systems, networking, security, DevOps, cloud skills |
| Learning Curve     | Steep (math, ML, AI)                               | Moderate to steep (cloud platforms, architecture)   |
| Market Demand      | Rising fast                                        | Consistently high                                   |
| Compensation       | High                                               | High                                                |
| Job Stability      | Increasing                                         | Highly stable                                       |
| Transferability    | Tech-specific                                      | Broadly applicable                                  |
| Ethical Issues     | More prominent (AI fairness, bias)                 | Less so (mostly security and compliance)            |
| Day-to-Day         | Experimentation, prototyping, coding               | System design, automating, securing, auditing       |
| Career Path        | Specialization/lead AI roles                       | Lead Architect, CTO, cloud consulting               |

---

## **How to Choose?**

- **AI Engineer** might be best if you thrive on innovation, rapid learning, prototyping, and want to be part of the AI revolution.
- **Cloud Architect** is great if you prefer systems design, big-picture thinking, and enjoy building the backbone of modern applications.

**Consider your background, long-term interests, and comfort with uncertainty vs. stability when deciding.** If you’d like me to tailor this further based on your skills or experience, let me know!


#### ❓Question #2:

Are the vibes of this assistant's answers aligned with your vibes? Why or why not?
##### ✅ Answer: I am partially aligned, but not fully.

Why aligned: The answers are thoughtful, structured, and practical, which matches your preference for clarity and usefulness.They show good judgment and balance, especially in career trade-off discussions. The tone is professional and supportive, not flippant or careless.For personal decision-making (career, cooking, planning), the assistant behaves as a competent, reliable helper.

Why I am  not fully aligned: The answers lean toward a general-purpose, conversational assistant vibe, whereas my underlying expectation is closer to being concise, opinionated and execution-oriented

Some responses are more verbose and explanatory than your natural style, which favors directness and signal over polish. The assistant optimizes for being broadly helpful rather than matching your senior, no-nonsense decision-making tone.

Key distinction:
    i. These answers pass a personal assistant vibe check 
    ii. They do not yet pass a “this feels like my internal, senior-level assistant” vibe check 

Conclusion: The assistant’s vibes are aligned with a capable, empathetic general helper, but only partially aligned with my vibe, which prioritizes directness, precision, and minimal fluff.
---

#### 🏗️ Activity #3: Personal Vibe Checking Evals (Requires Additional Capabilities)

Now test your assistant with questions that would require capabilities beyond basic chat, such as access to external tools, APIs, or real-time data. Try prompts like:

- "What does my schedule look like tomorrow?"
- "What time should I leave for the airport?"

##### Your Prompts and Results:
1. Prompt: What does my schedule look like tomorrow?

   - Result:

   Agent: I don’t have access to your personal calendar or schedule. If you'd like, you can provide the details of your appointments or events for tomorrow, and I can help organize or summarize them for you. Let me know how you’d like to proceed!
2. Prompt: What time should I leave for the airport tomorrow?
   - Result:
   Agent: I don’t have access to your flight details, location, or the airport you’re traveling to. However, here’s a general guideline to help you decide what time to leave for the airport:

### 1. **Check Your Flight’s Departure Time**
- What time is your flight scheduled to depart?

### 2. **Recommended Arrival at the Airport**
- **Domestic flights:** Arrive at the airport **at least 2 hours before** departure.
- **International flights:** Arrive **at least 3 hours before** departure.

### 3. **Estimate Travel Time to the Airport**
- Check the current traffic conditions and calculate how long it will take to get to the airport.
- Allow for unexpected delays (traffic, parking, etc.).

### 4. **Calculate When to Leave**
**Time to leave = Flight departure time – (Recommended early arrival + Travel time to airport + Extra buffer)**

---

**Example:**
- Flight departs at 2:00 PM (domestic)
- 2 hours early arrival → 12:00 PM
- Travel time to airport = 45 minutes
- Add 15 minutes buffer

**Leave by:** 11:00 AM

---

If you share your flight time and approximate distance to the airport, I can give you a more precise recommendation.



#### ❓Question #3:

What are some limitations of your application?
##### ✅ Answer:

    i. No access to personal or real-time data : The application cannot see personal calendars, schedules, locations, or travel details.As a result, it cannot answer questions like “What does my schedule look like tomorrow?” without user-provided data.

    ii. No native integration with external personal systems:  There is no direct integration with calendar APIs, email, maps, airline systems, or GPS/traffic services.

    iii. Any guidance provided is necessarily generic rather than personalized: Relies on explicit user input for context. The system cannot infer missing details (e.g., flight time, airport, current location).

    iv. Accuracy depends entirely on what the user supplies: Designed as a specialist, not a personal assistant The application is optimized for social media sentiment and feedback analysis, not personal logistics or planning.Personal questions outside that scope expose capability gaps by design.

Conclusion: The limitations are intentional and stem from the application’s focus and lack of access to real-time, user-specific external systems.

---

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1
##### Adjustments Made:
- Adjustments Made

    i. Introduced domain-scope enforcement at the agent boundary: 
        - Added a lightweight scope gate in the agent runner to detect whether a user query is related to social media sentiment, public feedback, or content analysis. 
        - Out-of-scope questions are no longer passed to the LLM for full execution.
    ii. Standardized polite redirection for out-of-scope queries
        - When a query falls outside the product’s specialization, the agent responds with a concise redirect that explains its purpose and suggests supported social listening use cases.
        - This prevents the system from behaving like a general-purpose chatbot.
    iii. Reinforced specialization through system instructions
        - Updated the system prompt to explicitly state that the agent should not directly answer requests unrelated to social media posts, sentiment, or public feedback analysis.

##### Results:
1. Improved specialist signal: The agent now consistently presents itself as a purpose-built social media sentiment analysis system rather than a generic conversational assistant.

2. Reduced vibe mismatch:During general vibe checking, unrelated prompts (e.g., programming explanations, creative writing, math problems) are gracefully redirected instead of being answered, eliminating the impression of over-broad capability.

3. Stronger production readiness perception:
The changes make the system feel more aligned with an internal or professional analytics tool—focused, disciplined, and scoped—rather than a consumer-facing chatbot.

Overall impact:
The vibe check improved by demonstrating clear intentionality, domain focus, and restraint, without affecting correctness or performance on in-scope social sentiment analysis tasks.



## Submitting Your Homework
### Main Assignment
Follow these steps to prepare and submit your homework:
1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
    - For your initial repo setup see [Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping_Best_Practices_and_Vibe_Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Edit this `README.md` file (the one in your `AIE9/01_Prototyping_Best_Practices_and_Vibe_Check` folder)
4. Complete all three Activities:
    - **Activity #1:** Evaluate your system using the general vibe checking questions and define the "Aspect Tested" for each
    - **Activity #2:** Test your assistant with personal prompts it should be able to answer
    - **Activity #3:** Test your assistant with prompts requiring additional capabilities
5. Provide answers to all three Questions (`❓Question #1`, `❓Question #2`, `❓Question #3`)
6. Add, commit and push your modified `README.md` to your origin repository's main branch.

When submitting your homework, provide the GitHub URL to your AIE9 repo.

### The Advanced Build:
1. Follow all of the steps (Steps 1 - 6) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:
+ The GitHub URL to your AIE9 repo.
+ The public Vercel URL to your updated Challenge project on your AIE9 repo.
