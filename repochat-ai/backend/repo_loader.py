import os, git, uuid
from code_chunker import chunk_code, is_code_file

def load_repo(repo_url, local_dir="repo"):
    if not os.path.exists(local_dir):
        git.Repo.clone_from(repo_url, local_dir)
    return local_dir

def extract_code_chunks(repo_path):
    documents = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            full_path = os.path.join(root, file)
            if is_code_file(full_path):
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        code = f.read()
                    for c in chunk_code(code):
                        documents.append({
                            "id": str(uuid.uuid4()),
                            "text": c,
                            "source": full_path.replace(repo_path, "")
                        })
                except Exception:
                    pass
    return documents
