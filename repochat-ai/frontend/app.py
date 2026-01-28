import streamlit as st, requests

BACKEND = "http://localhost:8000"

st.title("💬 RepoChat AI")
st.caption("Chat with any GitHub repository using GenAI + RAG")

repo_url = st.text_input("GitHub Repository URL")
if st.button("Index Repository"):
    r = requests.post(f"{BACKEND}/load_repo", json={"repo_url": repo_url})
    st.success(r.json())

st.divider()

question = st.text_input("Ask a question about the code")
if st.button("Ask"):
    r = requests.post(f"{BACKEND}/ask", json={"question": question})
    data = r.json()
    st.markdown("### Answer")
    st.write(data["answer"])
    st.markdown("### Sources")
    for s in data["sources"]:
        st.write(f"- `{s}`")
