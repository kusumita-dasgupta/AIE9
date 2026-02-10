# AI Life Coach with Multi-Domain Expertise  
Deep Agents – Advanced Build

This project implements an **AI Life Coach** built using the Deep Agents architecture.  
The system provides personalized guidance across multiple life domains with persistent memory and adaptive planning.

---

# Architecture Overview

The system follows a **Coordinator + Specialist Subagent** architecture.

The **Life Coach Coordinator** orchestrates planning, memory, and workflow while delegating domain-specific tasks to specialist subagents.

## Components

**Coordinator**
- Life Coach (main Deep Agent)
- Handles assessment, planning, integration, and progress tracking

**Specialist Subagents**
- Career Coach → job search, skills, growth strategy
- Relationship Coach → communication, boundaries, social health
- Finance Coach → budgeting, saving, priorities
- Wellness Coach → health, fitness, stress, sleep

---

## Architecture Diagram

```mermaid
flowchart TB
  U[User] --> C[Life Coach Coordinator]

  C -->|delegates| CC[Career Coach]
  C -->|delegates| RC[Relationship Coach]
  C -->|delegates| FC[Finance Coach]
  C -->|delegates| WC[Wellness Coach]

  C --> FS[(Workspace Filesystem)]
  C --> MS[(LangGraph Store Memory)]

  FS --> P[plans/]
  FS --> A[assessments/]
  FS --> PR[progress/]
  FS --> UP[user_profile/]
  FS --> R[resources/]


