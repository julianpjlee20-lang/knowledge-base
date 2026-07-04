import subprocess
import os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(base)

try:
    subprocess.run(["git", "add", "claude/"], check=True)
    subprocess.run(["git", "commit", "-m", "auto: session sync"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("✅ 已同步到 GitHub")
except subprocess.CalledProcessError:
    print("⚠️ 同步失敗或無新變更")
