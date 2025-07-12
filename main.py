import os
import subprocess

# Set your desired date
date = "2025-07-15T12:00:00"

os.environ["GIT_AUTHOR_DATE"] = date
os.environ["GIT_COMMITTER_DATE"] = date

# Create a dummy file change
with open("hello.txt", "a") as f:
    f.write(f"Commit for {date}\n")

# Git commit
subprocess.run(["git", "add", "hello.txt"])
subprocess.run(["git", "commit", "-m", f"Commit for {date}"])
subprocess.run(["git", "push", "origin", "main"])

