
import ollama

from database import cursor
from schema import get_schema
from sql_validator import validate_sql


def generate_sql(user_question):

    database_info = get_schema()

    prompt = f"""
You are an SQL assistant.

Database information:
{database_info}

User question:
{user_question}

Generate only the SQL query needed to answer the question.
Do not explain anything.
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    sql = response["message"]["content"].strip()

    if sql.startswith("```"):
        sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql


def fix_sql(user_question, bad_sql, error_message):

    database_info = get_schema()

    prompt = f"""
You are an SQL debugging assistant.

DATABASE SCHEMA:
{database_info}

USER QUESTION:
{user_question}

INCORRECT SQL:
{bad_sql}

DATABASE ERROR:
{error_message}

Fix the SQL query.

IMPORTANT:
- Use only tables and columns from the database schema.
- Check every column against the schema.
- Do not invent columns.
- Return ONLY the corrected SQL query.
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    sql = response["message"]["content"].strip()

    if sql.startswith("```"):
        sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql


def format_result(result):

    if not result:
        return "No results found."

    # Single value
    if len(result[0]) == 1:
        value = result[0][0]

        if isinstance(value, (int, float)):
            return f"The answer is {value:,}."

        return str(value)

    # Multiple rows / columns
    lines = []

    for row in result:

        formatted_row = " | ".join(
            f"{value:,}" if isinstance(value, (int, float))
            else str(value)
            for value in row
        )

        lines.append(formatted_row)

    return "\n".join(lines)


def ask_database(user_question):

    # Generate SQL
    sql = generate_sql(user_question)

    # Validate SQL
    if not validate_sql(sql):
        return "The generated SQL was rejected for safety."

    # Execute SQL
    try:

        cursor.execute(sql)
        result = cursor.fetchall()

    except Exception as e:

        # Try to fix the SQL
        corrected_sql = fix_sql(
            user_question,
            sql,
            str(e)
        )

        # Validate corrected SQL
        if not validate_sql(corrected_sql):
            return "The corrected SQL was rejected for safety."

        # Execute corrected SQL
        try:

            cursor.execute(corrected_sql)
            result = cursor.fetchall()

        except Exception as e2:

            return f"SQL failed after correction: {e2}"

    # Format result
    return format_result(result)


DATABASE_RULES = """
Important SQL rules:

1. Use only tables and columns provided in the database schema.
2. Do not invent columns.
3. Do not join tables unless the question requires data from multiple tables.
4. order_items.price contains the item price.
5. order_items.order_item_id is an item sequence number, NOT a quantity or price.
6. For total revenue from order items, use SUM(order_items.price).
7. Generate the simplest correct SQL query possible.
"""


def generate_sql(user_question):

    database_info = get_schema()

    prompt = f"""
You are an SQL assistant.

DATABASE INFORMATION:
{database_info}

IMPORTANT DATABASE RULES:
{DATABASE_RULES}

USER QUESTION:
{user_question}

Generate only the SQL query needed to answer the question.
Do not explain anything.
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    sql = response["message"]["content"].strip()

    if sql.startswith("```"):
        sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql


def fix_sql(user_question, bad_sql, error_message):

    database_info = get_schema()

    prompt = f"""
You are an SQL debugging assistant.

DATABASE SCHEMA:
{database_info}

IMPORTANT DATABASE RULES:
{DATABASE_RULES}

USER QUESTION:
{user_question}

INCORRECT SQL:
{bad_sql}

DATABASE ERROR:
{error_message}

Your job is to completely rewrite the incorrect SQL.

IMPORTANT:
- Check every table and column against the database schema.
- Do not invent columns.
- Do not reuse incorrect columns from the old query.
- Do not join tables unless required.
- Return ONLY the corrected SQL query.
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    sql = response["message"]["content"].strip()

    if sql.startswith("```"):
        sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql
