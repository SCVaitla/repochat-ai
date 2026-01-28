import os

def chunk_code(text, max_lines=40, overlap=10):
    lines = text.splitlines()
    chunks = []
    i = 0
    while i < len(lines):
        chunk = lines[i:i + max_lines]
        chunks.append("\n".join(chunk))
        i += max_lines - overlap
    return chunks

def is_code_file(path):
    return path.endswith((
        ".py", ".js", ".ts", ".jsx", ".tsx",
        ".java", ".cpp", ".c", ".h",
        ".go", ".rs"
    ))
