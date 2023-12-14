import sqlite3
from langchain.tools import Tool

conn = sqlite3.connect('src/agent/db.sqlite')

def list_tables():
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    rows = c.fetchall()
    return "\n".join(row[0] for row in rows if row[0] is not None)

def run_sqlite_query(query):
    c = conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()

    except sqlite3.OperationalError as e:
        return f"次のエラーが発生しました{str(e)}"

run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="SQLiteのクエリを実行します",
    func=run_sqlite_query,
)

def describe_tables(table_names):
    c = conn.cursor()
    tables = ', '.join("'" + table + "'" for table in table_names)
    rows = c.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name IN ({tables});")
    return '\n'.join(row[0] for row in rows if row[0] is not None)


describe_tables_tool = Tool.from_function(
    name="describe_tables",
    description="テーブルの構造を説明します",
    func=describe_tables,
)