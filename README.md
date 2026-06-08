# AI Agent with Tools

A beginner-friendly Python CLI AI agent that can use tools such as a calculator, note saver, and file reader.

## Goal

This project demonstrates how an AI agent can:
- receive a user request
- decide whether a tool is needed
- call the correct tool
- use the tool result to answer the user

## Tech Stack

- Python
- OpenAI API
- python-dotenv
- Git and GitHub

# AI Agent With Tools

A beginner-friendly Python CLI AI agent that can use tools, remember conversations, read files, and maintain persistent memory.

## Project Goal

This project demonstrates how an AI agent works internally:

* Receive user input
* Decide whether to use tools
* Execute tools
* Use tool results to generate final answers
* Store conversation history
* Persist memory between sessions

---

## Features Implemented

### Core Agent Features

* CLI chatbot
* OpenAI API integration
* Tool selection using prompting
* Tool execution loop
* Conversation memory during runtime
* Persistent memory across sessions
* Clear memory command

### Available Tools

#### Calculator Tool

Supports:

* Addition
* Subtraction
* Multiplication
* Division
* Powers

Implemented safely using Python AST parsing instead of `eval()`.

#### Note Memory Tool

Can:

* Save notes
* Read saved notes

Uses:

```text
notes.txt
```

#### File Reader Tool

Can:

* Read local files
* Summarize file contents
* Inspect text files

Examples:

```text
Read sample.txt
Summarize README.md
```

---

## Project Structure

```text
ai-agent-with-tools/
│
├── agent/
│   ├── __init__.py
│   └── prompts.py
│
├── main.py
├── tools.py
├── memory.py
├── README.md
├── sample.txt
├── .env
├── .gitignore
└── venv/
```

---

## Setup

Create environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install openai python-dotenv
```

Create `.env`:

```env
OPENAI_API_KEY=your_key_here
```

Run:

```bash
python main.py
```

---

## Example Usage

Calculator:

```text
What is 50 * 4?
```

Memory:

```text
Remember that my favorite food is pizza
```

Files:

```text
Read sample.txt
```

Clear memory:

```text
clear memory
```

Exit:

```text
exit
```

---

## Current Limitations

* Tool calling depends on prompt formatting
* Memory grows forever
* No structured tool schemas
* No multi-step reasoning
* Limited file support
* Single-agent architecture

---

## Future Improvements

* Structured tool calling
* Memory compression
* Better file handling
* Multi-tool workflows
* Multi-agent architecture
* Retrieval augmented generation (RAG)
* Web search tools
* Better logging and observability

---

