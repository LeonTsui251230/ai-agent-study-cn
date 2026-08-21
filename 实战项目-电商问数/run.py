"""入口。"""
from text2sql import question_to_sql
from query import run_sql
from chart import draw_bar

if __name__ == "__main__":
    q = input("用自然语言提问：")
    sql = question_to_sql(q)
    print("生成 SQL:", sql)
    rows, cols = run_sql(sql)
    draw_bar(rows, cols)
