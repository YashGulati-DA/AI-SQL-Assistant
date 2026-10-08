
def validate_sql(sql):

    sql = sql.strip()

    # Must start with SELECT
    if not sql.upper().startswith("SELECT"):
        return False

    # Remove one optional semicolon at the end
    if sql.endswith(";"):
        sql = sql[:-1].strip()

    # No semicolons should remain
    if ";" in sql:
        return False

    return True
