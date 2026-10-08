# AI-Powered SQL Query Assistant

An AI-powered data analytics assistant that converts natural-language business questions into SQL queries, executes them on a SQLite database, and returns the exact result.

## Project Overview

This project uses a local Large Language Model (LLM) to understand natural-language questions and generate SQL queries dynamically.

The generated SQL is validated and executed against an Olist e-commerce SQLite database.

If the generated SQL fails, the LLM is asked to correct the query and the system retries it.

Python handles the final database result so that numerical answers come directly from the database.

## Architecture

```text
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
```

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
- SQL
- SQLite
- Ollama
- Llama 3.2
- Pandas
- Jupyter Notebook

## Project Structure

```text
AI-SQL-Assistant/
│
├── data/
│   ├── olist_dataset/
│   └── olist.db
│
├── notebooks/
│   └── olist_ai.ipynb
│
├── src/
│   ├── assistant.py
│   ├── database.py
│   ├── schema.py
│   └── sql_validator.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## How It Works

### 1. User asks a question

For example:

```text
What is the total revenue from all orders?
```

### 2. Database schema is provided to the LLM

The system discovers the available tables and columns from the SQLite database and provides this information to the LLM.

### 3. LLM generates SQL

For example:

```sql
SELECT SUM(order_items.price)
FROM order_items;
```

### 4. SQL is validated

The generated SQL is checked by the SQL validation layer before execution.

### 5. SQL is executed

The validated query is executed against the SQLite database.

### 6. SQL errors can be corrected

If the generated SQL fails, the error message, original question, and incorrect SQL are sent back to the LLM so it can generate a corrected query.

The system then retries the corrected query.

### 7. Python formats the result

The final result is taken directly from SQLite and formatted by Python.

This prevents the LLM from changing or hallucinating numerical database results.

## Example Questions

The assistant can answer questions such as:

- How many customers are there?
- How many orders have been delivered?
- What is the total revenue from all orders?
- Which payment method is most popular?
- Show the number of payments for each payment method.

## Example

**User:**

```text
What is the total revenue from all orders?
```

**Generated SQL:**

```sql
SELECT SUM(order_items.price)
FROM order_items;
```

**Assistant:**

```text
The answer is 13,591,643.7.
```

Another example:

**User:**

```text
How many customers are there?
```

**Assistant:**

```text
The answer is 99,441.
```

## Setup

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Ollama

Install Ollama and download the Llama 3.2 model.

Run:

```bash
ollama run llama3.2:3b
```

Make sure Ollama is running before using the assistant.

### 3. Prepare the dataset

Download the Olist Brazilian E-Commerce Public Dataset and place the extracted dataset inside:

```text
data/olist_dataset/
```

The SQLite database should be available at:

```text
data/olist.db
```

### 4. Run the notebook

Open:

```text
notebooks/olist_ai.ipynb
```

Run the notebook cells to test the assistant.

## Dataset

The project uses the Olist Brazilian E-Commerce Public Dataset.

The dataset and SQLite database are used locally and are not included in the GitHub repository because of their size.

## Safety

The assistant is designed for read-only SQL queries.

The SQL validator currently allows queries beginning with:

```sql
SELECT
```

and rejects queries containing multiple SQL statements.

This helps prevent destructive SQL operations such as:

```sql
DELETE
UPDATE
DROP
INSERT
```

from being executed by the assistant.

## Future Improvements

- Streamlit user interface
- Better result formatting
- Query history
- More advanced SQL validation
- Support for larger databases
- RAG-based schema retrieval
- Agentic workflows
