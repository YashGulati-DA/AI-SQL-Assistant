
# AI-Powered SQL Query Assistant

An AI-powered data analytics assistant that converts natural-language business questions into SQL queries, executes them on a SQLite database, and returns the exact result.

## Project Overview

This project uses a local Large Language Model (LLM) to understand natural-language questions and generate SQL queries dynamically.

The generated SQL is validated and executed against an Olist e-commerce SQLite database.

If the generated SQL fails, the LLM is asked to correct the query and the system retries it.

## Architecture

User Question
        ↓
Llama 3.2 LLM
        ↓
SQL Generation
        ↓
SQL Validation
        ↓
SQLite Database
        ↓
SQL Result
        ↓
Python Formatting
        ↓
Final Answer

## Features

- Natural-language to SQL generation
- Automatic database schema discovery
- SQLite database integration
- SQL safety validation
- Automatic SQL error correction
- Exact database results
- Local LLM using Ollama
- Dynamic business questions
- Olist Brazilian E-Commerce dataset

## Technologies Used

- Python
- SQLite
- Ollama
- Llama 3.2
- Pandas
- Jupyter Notebook
- SQL

## Project Structure

AI-SQL-Assistant/

├── data/

├── notebooks/

│   └── olist_ai.ipynb

├── src/

│   ├── database.py

│   ├── schema.py

│   ├── sql_validator.py

│   └── assistant.py

├── requirements.txt

├── .gitignore

└── README.md

## Example Questions

The assistant can answer questions such as:

- How many customers are there?
- How many orders have been delivered?
- What is the total revenue from all orders?
- Which payment method is most popular?
- Show the number of payments for each payment method.

## Example

User:

What is the total revenue from all orders?

Assistant:

The answer is 13,591,643.7.

## Dataset

The project uses the Olist Brazilian E-Commerce Public Dataset.

The dataset is used locally and is not included in the GitHub repository.

## Future Improvements

- Streamlit user interface
- Better result formatting
- Query history
- More advanced SQL validation
- Support for larger databases
- RAG-based schema retrieval
- Agentic workflows
