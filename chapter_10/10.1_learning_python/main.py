from pathlib import Path

path = Path("learning_python.txt")
content = path.read_text()
"""Printing the entire file"""
print(content)

"""Printing line by line"""
split_content = content.splitlines()

for line in split_content:
    print(line)
