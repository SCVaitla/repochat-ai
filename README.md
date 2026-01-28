RepoChat AI

GenAI-Powered GitHub Repository Q&A using Retrieval-Augmented Generation (RAG)

RepoChat AI is a GenAI application that allows users to chat with a GitHub codebase.
It indexes source code from a repository, retrieves relevant code snippets using vector search, and generates grounded, context-aware answers using a large language model.

This project demonstrates how LLMs can be safely applied to real software engineering workflows using Retrieval-Augmented Generation (RAG) to reduce hallucinations.

Key Features

- Clone and index any public GitHub repository

- Chunk and embed source code files

- Semantic search using FAISS vector database

- Natural-language Q&A over the codebase

- File-level source references in every answer

- Clean backend–frontend separation

Why This Project Matters

This project reflects real-world GenAI system design.

It demonstrates:

- Retrieval-Augmented Generation (RAG)

- Large codebase understanding

- LLM grounding and hallucination control

- Backend API design with FastAPI

- Practical AI applied to software engineering

This is the same architectural pattern used in internal developer tools at large tech companies.

Architecture Overview

User Question
   ↓
Streamlit Frontend
   ↓
FastAPI Backend
   ↓
FAISS Vector Search (Code Embeddings)
   ↓
Relevant Code Chunks
   ↓
LLM (GPT-4o-mini)
   ↓
Answer + Source Files

