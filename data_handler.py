import json

db = {}
def load_data():
    with open("save.json",  'r' ) as f:
        lines = f.readlines()
        for line in lines:
            todo_id, task = line.strip()