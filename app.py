import sys
from pathlib import Path

import streamlit as st

# Make the src folder importable when Streamlit runs from the project root.
BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from assistant import ask_database


st.set_page_config(
    page_title="AI SQL Assistant",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 AI-Powered SQL Query Assistant")
st.write("Ask a natural-language question about the Olist e-commerce database.")

st.info("Make sure Ollama is running with the `llama3.2:3b` model before asking a question.")

examples = [
    "How many customers are there?",
    "How many orders have been delivered?",
    "What is the total revenue from all orders?",
    "Show the number of payments for each payment method.",
]

st.subheader("Try an example")

example = st.selectbox(
    "Choose a question",
    [""] + examples,
)

question = st.text_area(
    "Your question",
    value=example,
    placeholder="Example: What is the total revenue from all orders?",
    height=100,
)

if st.button("Ask AI", type="primary", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Generating SQL and querying the database..."):
            try:
                answer = ask_database(question.strip())

                st.subheader("Answer")
                st.success(answer)

            except Exception as e:
                st.error(f"Something went wrong: {e}")

st.divider()

st.caption("Built with Python, Streamlit, Ollama (Llama 3.2), and SQLite.")
