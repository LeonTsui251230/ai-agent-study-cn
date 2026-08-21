"""受控执行 SQL（只允许 SELECT）。"""
import sqlite3


def run_sql(sql: str, db_path: str = "sample.db"):
    if not sql.strip().lower().startswith("select"):
        raise ValueError("仅允许 SELECT 查询")
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.execute(sql)
        return cur.fetchall(), [d[0] for d in cur.description]
    finally:
        conn.close()
