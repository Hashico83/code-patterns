
# Multi-Agent Critique System (Reference Version)

> **Note:** This implementation was built by me to be more clear on the implementation of multi agent. Consider this as a starting point and scaffolding code to get an idea of how agents call and how self prompting to enable an agent to assume multiple personas. This is for my **learning purposes only**. In the next iteration will enhance the implementation with Tools usage and decision making for multiple agents usage.

---

## 📌 Project Overview
This project implements a **simple multi-agent system** where:
- A **Coordinator Agent** receives a paragraph and a list of personas from the user.
- For each persona, a **Critique Agent**:
  - Loads persona-specific instructions from YAML.
  - Performs **self-prompting** (draft → refine) to generate high-quality critique.
- The Coordinator aggregates all critiques and returns both **raw JSON** and **formatted Markdown output**.

---

## ✅ Key Principles Demonstrated

### 1. Persona Pattern
**What is it?**
- A design pattern where agents assume specific roles or expertise areas (personas) to perform tasks.

**Why is it important?**
- It allows modularity and specialization in multi-agent systems.

**How is it implemented here?**
- Each persona is defined in a separate YAML file under `config/personas/`.
- Example:
```yaml
description: "You are a grammar specialist. 
Critique the text for syntax, punctuation, and clarity."
```


 ### 2. Self-Prompting
**What is it?**

A technique where an agent iteratively improves its own output by prompting itself.

**Why is it important?**

It enhances reasoning and output quality without human intervention.

**How is it implemented here?**

***Stage 1: Generate initial critique.***

Prompt:
```
You are {persona_description}.
Critique the following text:
"{paragraph}"
Return in structured format:
Strengths:
- ...
Weaknesses:
- ...
Suggestions for Improvement:
- ...
```

***Stage 2: Refine the critique.***

```
Here is your initial critique:
"{draft_critique}"
Review and improve:
- Add actionable suggestions.
- Ensure clarity and depth.
```

**📂 Folder Structure**

```
│multi-agent-critique/
├── config/
│   └── personas/
│       ├── grammar_expert.yaml
│       ├── technical_reviewer.yaml
│       └── creative_coach.yaml
│
├── src/
│   ├── main.py              # Interactive CLI
│   ├── coordinator.py       # Coordinator Agent
│   ├── critique_agent.py    # Critique Agent with self-prompting
│   ├── utils/
│   │   └── formatter.py     # Markdown formatting
│   └── models/
│       └── llm.py           # LLM client (ChatGPT/Gemini)
│
└── requirements.txt
```

**▶ How to Run**

***Install dependencies:***

```pip install -r requirements.txtShow more lines```

***Set API keys:***

```
export OPENAI_API_KEY="your_openai_key"
export GOOGLE_API_KEY="your_gemini_key"Show more lines
```
***Run the CLI:***

```
python src/main.py
```
 ## 🎯 Learning Objectives

Understand Persona Pattern for role-based agent design.

Implement Self-Prompting for iterative reasoning.

Build a modular architecture for multi-agent systems.

Prepare for enhancements like:

Dynamic persona selection.

Tool integration.

Autonomous decision-making.