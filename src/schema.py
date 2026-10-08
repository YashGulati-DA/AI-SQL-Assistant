
from database import cursor


def get_schema():

    cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table';
    """)

    tables = cursor.fetchall()

    schema = ""

    for table in tables:

        table_name = table[0]

        cursor.execute(f"PRAGMA table_info({table_name})")

        columns = cursor.fetchall()

        schema += f"TABLE: {table_name}\n"

        for column in columns:
            schema += f"{column[1]} {column[2]}\n"

        schema += "\n"

    return schema
