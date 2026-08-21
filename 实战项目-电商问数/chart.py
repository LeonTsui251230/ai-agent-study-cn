"""把查询结果画成简单柱状图（示意）。"""
def draw_bar(rows, columns, title="结果"):
    # 实际可用 matplotlib 绘制并保存
    print(f"[{title}] 列: {columns}")
    for r in rows:
        print("  ", r)
