import os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 讀取並輸出 index.md 給 Claude
index_path = os.path.join(base, "claude", "index.md")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        print(f.read())
