import streamlit as st
import os

from ingest import create_vector_store
from query import ask_question

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Document Assistant")
st.caption("Upload documents and chat with them")

# Sidebar
with st.sidebar:

    st.header("📂 Upload Documents")

    uploaded_files = st.file_uploader(
        "Upload PDF or DOCX",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    if uploaded_files:

        os.makedirs("temp", exist_ok=True)

        paths = []

        for file in uploaded_files:

            path = os.path.join("temp", file.name)

            with open(path, "wb") as f:
                f.write(file.getbuffer())

            paths.append(path)

        if st.button("Process Documents"):

            with st.spinner("Creating knowledge base..."):

                create_vector_store(paths)

            st.success("Documents ready!")

st.divider()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Ask something about the documents")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer, sources = ask_question(question)

        st.write(answer)

        st.markdown("**Sources:**")

        for s in sources:
            st.write("📄", s)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

# Download conversation
if st.session_state.messages:

    chat_text = ""

    for msg in st.session_state.messages:
        chat_text += f"{msg['role']}: {msg['content']}\n\n"

    st.download_button(
        "Download Chat",
        chat_text,
        file_name="chat_history.txt"
    )