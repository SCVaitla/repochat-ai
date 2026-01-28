import os, faiss, numpy as np
from sentence_transformers import SentenceTransformer
from openai import OpenAI

client = OpenAI()
model = SentenceTransformer("all-MiniLM-L6-v2")
dim = model.get_sentence_embedding_dimension()
index = faiss.IndexFlatL2(dim)
documents = []

def add_documents(docs):
    global documents
    embeddings = model.encode([d["text"] for d in docs])
    index.add(np.array(embeddings).astype("float32"))
    documents.extend(docs)

def ask_question(question, k=5):
    q_emb = model.encode([question])
    _, I = index.search(np.array(q_emb).astype("float32"), k)
    context, sources = [], []
    for idx in I[0]:
        doc = documents[idx]
        context.append(doc["text"])
        sources.append(doc["source"])
    prompt = f'''
You are an expert software engineer.
Answer ONLY using the context below.
If not found, say "I don’t know".

Context:
{chr(10).join(context)}

Question:
{question}
'''
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content, list(set(sources))
