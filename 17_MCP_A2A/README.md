<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">Session 17: Model Context Protocol (MCP) & Agent-to-Agent (A2A) Protocol</h1>

| Session Sheet | Recording     | Slides        | Repo         | Homework      | Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [MCP Servers & A2A](../00_Docs/Session_Sheets/17_MCP_Servers_and_A2A) |[Recording!](https://us02web.zoom.us/rec/share/_iJT-kZiYacyz23fjU3N7w7mZIUFJqGXV48RDqCkCY3avsmngKtzK0SNs0I7k74.xICq6NSv6l6GqAFU) <br> passcode: `fJ9tx4h.`| [Session 17 Slides](https://www.canva.com/design/DAG-ELapG4g/6vDMm63RBwKVsSZvheorVA/edit?utm_content=DAG-ELapG4g&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [(Optional) Session 17 Assignment: MCP Servers & A2A](https://forms.gle/qtjQFfoEF8aykTWy5) | [Feedback 3/12](https://forms.gle/sJwD1a6LLn9NU9s48) |
---

## 📚 Useful Resources

**MCP (Model Context Protocol)**
- [MCP Official Docs](https://modelcontextprotocol.io/) — Spec, tutorials, and guides
- [MCP-UI](https://mcpui.dev/) — Official standard for interactive UI in MCP
- [MCP Auth Guide (Auth0)](https://auth0.com/blog/mcp-specs-update-all-about-auth/) — Deep dive into MCP auth spec updates

**A2A (Agent-to-Agent Protocol)**
- [A2A Official Docs](https://a2a-protocol.org/latest/) — Spec and guides
- [A2A GitHub Repo](https://github.com/a2aproject/A2A) — Protocol spec and implementations
- [Announcing A2A (Google Blog)](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) — Protocol vision and motivation

**MCP vs A2A**
- [A2A and MCP (Official)](https://a2a-protocol.org/latest/topics/a2a-and-mcp/) — How they complement each other

---

# Running the MCP Server

### 1. Install dependencies

```bash
uv sync
```

### 2. Set up environment variables

Copy the example env file and fill in your OpenAI API key:

```bash
cp .env.example .env
```

### 3. Run the MCP server locally

```bash
uv run server.py
```

The server will start on `http://localhost:8000`.

### 4. Expose the server with ngrok (for remote/Claude Desktop access)

In a separate terminal, start an ngrok tunnel:

```bash
ngrok http 8000
```

Copy the ngrok forwarding URL (e.g. `https://xxxx-xx-xx-xx-xx.ngrok-free.app`) and restart the server with it:

```bash
ISSUER_URL=https://xxxx-xx-xx-xx-xx.ngrok-free.app uv run server.py
```

> **Note:** The `ISSUER_URL` must match the public URL clients use to reach the server, otherwise OAuth authentication will fail.

---

# Build 🏗️

In today's assignment, we'll be building an MCP server with OAuth authentication — a cat shop application that exposes tools for browsing products, managing a cart, and checking out.

- 🤝 Breakout Room #1
  - Set up the MCP server with OAuth and the product database
  - Explore the MCP tools: `list_products`, `get_product`, `add_to_cart`, `view_cart`, `remove_from_cart`, `checkout`

- 🤝 Breakout Room #2
  - Connect an MCP client to the server
  - Build an end-to-end interaction flow using the MCP tools

# Ship 🚢

The completed MCP server and client integration!

### Deliverables

- A short Loom of either:
  - the MCP server you built and a demo of the client interacting with it; or
  - the notebook you created for the Advanced Build

# Share 🚀

Make a social media post about your final application!

### Deliverables

- Make a post on any social media platform about what you built!

Here's a template to get you started:

```
🚀 Exciting News! 🚀

I am thrilled to announce that I have just built and shipped an MCP server with OAuth authentication! 🎉🤖

🔍 Three Key Takeaways:
1️⃣ I learned how MCP servers expose tools in a standardized way so AI clients can securely interact with application functionality like product browsing and cart management.
2️⃣ I learned why OAuth is critical in MCP: it authenticates the client and ensures tool actions are performed in the correct user context instead of allowing unauthenticated access.
3️⃣ I learned the difference between MCP and A2A: MCP is for agent-to-tool/service interaction, while A2A is for communication and coordination between independent agents.

Let's continue pushing the boundaries of what's possible in the world of AI and tool integration. Here's to many more innovations! 🚀
Shout out to @AIMakerspace !

#MCP #ModelContextProtocol #OAuth #Innovation #AI #TechMilestone

Feel free to reach out if you're curious or would like to collaborate on similar projects! 🤝🔥
```

# Submitting Your Homework [OPTIONAL]

## Main Homework Assignment

Follow these steps to prepare and submit your homework assignment:

1. Review the MCP server code in `server.py` and the `app/` directory
2. Run the MCP server locally using `uv run server.py`
3. Connect to the server using an MCP client (e.g., Claude Desktop, or a custom client)
4. Test all available tools: browsing products, adding to cart, viewing cart, removing items, and checkout
5. Record a Loom video reviewing what you have learned from this session

## Questions

### ❓ Question #1:

Why is OAuth important for MCP servers, and what security considerations should you keep in mind when exposing tools to AI clients?

#### ✅ Answer:

OAuth is important for MCP servers because it provides a secure authentication and authorization mechanism that ensures only verified clients or users can access the tools exposed by the MCP server. Since MCP servers allow AI agents to call real system capabilities such as databases, APIs, or transactional operations, OAuth helps enforce identity verification and permission boundaries before any tool is executed.

When exposing tools to AI clients, several security considerations are important. First, tools should follow the principle of least privilege, meaning the AI client should only have access to the minimal set of operations required. Second, sensitive operations such as payments or data modifications should require additional validation or user confirmation. Third, proper input validation and schema enforcement should be used to prevent malicious or unintended tool usage. Finally, secure token management and HTTPS communication should be enforced to prevent credential leakage and unauthorized access.

### ❓ Question #2:

What is the Agent-to-Agent (A2A) protocol, and how does it differ from MCP in terms of purpose and architecture? When would you choose A2A over MCP?

#### ✅ Answer:

The Agent-to-Agent (A2A) protocol is a communication framework that allows independent AI agents to discover, communicate with, and delegate tasks to other agents in a standardized way. It enables agents to exchange capabilities, coordinate workflows, and collaborate across systems using agent cards and interoperable protocols.

A2A differs from MCP in its purpose and architecture. MCP is primarily designed for connecting an AI client to tools, resources, or services exposed by a server. It focuses on enabling an agent to use structured tools such as APIs or databases. A2A, on the other hand, focuses on communication between autonomous agents rather than tool invocation. In A2A architectures, agents can delegate tasks, request capabilities from other agents, and coordinate complex workflows across distributed systems.

You would choose A2A when building multi-agent systems where different agents specialize in different tasks and need to collaborate with each other. MCP is better suited for cases where a single agent needs to access tools or services exposed by a server.
## Activity 1: Extend the MCP Server

Add at least one new tool to the cat shop MCP server (e.g., `search_products`, `update_cart_quantity`, or `get_order_history`). Ensure the new tool integrates properly with the existing database and OAuth authentication. Demo the new tool through an MCP client and include it in your Loom video.

## Advanced Activity: Build a Custom MCP Client

Build a custom MCP client that connects to the cat shop server over Streamable HTTP, authenticates via OAuth, and orchestrates a multi-step shopping flow (browse → add to cart → checkout). Compare the developer experience of MCP-based tool integration vs. traditional REST API calls.

Include your findings and a demo in your Loom video.

I extended the MCP server by adding a new tool called update_cart_quantity(product_id, quantity). I implemented the tool in app/tools.py, where the existing MCP tools are already defined. The tool integrates with the existing SQLite database by updating records in the cart_items table. It also integrates with the existing OAuth authentication flow by using the current _get_username() helper, which maps the access token to the authenticated user before performing the cart update. This ensures the cart modification is scoped to the logged-in user and remains protected by the same authenticated MCP server setup.
