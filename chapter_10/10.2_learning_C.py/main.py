from pathlib import Path

path = "learning_python.txt"

with open(path) as p:
    lines = p.readlines()


for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C'))
