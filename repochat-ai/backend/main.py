from fastapi import FastAPI
from pydantic import BaseModel
from repo_loader import load_repo, extract_code_chunks
from rag import add_documents, ask_question

app = FastAPI(title="RepoChat AI")

class RepoRequest(BaseModel):
    repo_url: str

class QuestionRequest(BaseModel):
    question: str

@app.post("/load_repo")
def load_repository(req: RepoRequest):
    path = load_repo(req.repo_url)
    docs = extract_code_chunks(path)
    add_documents(docs)
    return {"status": "indexed", "chunks": len(docs)}

@app.post("/ask")
def ask(req: QuestionRequest):
    answer, sources = ask_question(req.question)
    return {"answer": answer, "sources": sources}
