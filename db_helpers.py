from psycopg2.extras import RealDictCursor
from database import get_connection

conn = get_connection()


def fetch_all(query: str, params: tuple = ()) -> list[dict]:
    print(params)
    """Run a SELECT query and return all rows as list of dicts."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(query, params)
        return cur.fetchall()


def fetch_one(query: str, params: tuple = ()) -> dict | None:
    """Run a SELECT query and return a single row as dict."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(query, params)
        return cur.fetchone()


def insert_record(table: str, data: dict, returning: str = "*") -> dict:
    """Insert a record into a table and return the inserted row."""
    cols = ", ".join(data.keys())
    placeholders = ", ".join(["%s"] * len(data))
    values = tuple(data.values())
    query = f"INSERT INTO {table} ({cols}) VALUES ({placeholders}) RETURNING {returning};"
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(query, values)
        new_row = cur.fetchone()
        conn.commit()
        return new_row


def delete_record(table: str, condition: str, params: tuple = ()) -> dict | None:
    """Delete a record and return the deleted row (if any)."""
    query = f"DELETE FROM {table} WHERE {condition} RETURNING *;"
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(query, params)
        deleted = cur.fetchone()
        conn.commit()
        return deleted
