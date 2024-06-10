from flask import Flask, request, jsonify
import random
import json
import pytest

app = Flask(__name__)

def load_database():
    with open('save.json') as file:
        return json.load(file)

def save_database():
    with open('save.json', 'w') as file:
        return json.dump(tasks, file)

tasks = load_database()


@app.route('/tasks', methods=["GET"])
def get_tasks():
    return jsonify(list(tasks.values())), 200


@app.route('/addtask/<new_task>', methods=["POST"])
def add_task(new_task):
    id = random.randint(1000, 9999)
    tasks.update({id: new_task})
    save_database()
    return jsonify({id:new_task}),200

@app.route('/check', methods=["GET"])
def check():
    ids = request.get_json()
    return_dict = {}
    for id in ids:
        if id in tasks:
            status_dict = {id: {"task" : tasks[id], "exists" : True}}
            return_dict.update(status_dict)
        else:
            status_dict = {id: {"task" : None , "exists" : False}}
            return_dict.update(status_dict)

    return jsonify(return_dict),200

@app.route('/removetask', methods=["DELETE"])
def remove_task():
    return_dict= {}
    ids = request.get_json()
    print(ids)
    for id in ids:
        if id in tasks:
            del tasks[id]
            save_database()
            status_dict = {id:{"removed" : True}}
            return_dict.update(status_dict)    
    return jsonify(return_dict), 200

if __name__ == '__main__':
    app.run(debug=True)
