from flask import Flask, request, jsonify
import random



app = Flask(__name__)
#reads in the save.txt file and populates a dictionary based on the id and task
def read():
    tasks={}
    with open('save.txt', 'r') as file:
            for line in file:
                id, task = line.strip().split(",")
                tasks[id] = task
    return tasks
#saves tasks dictionary with any added or removed tasks
def save(tasks):
    with open('save.txt', 'w') as file:
        for id, task in tasks.items():
            file.write(f"{id},{task}\n")

tasks = read()


@app.route('/tasks', methods=["GET"])
def get_tasks():
    return list(tasks.values())

@app.route('/addtask/<new_task>', methods=["POST"])
def add_task(new_task):
    id = random.randint(1000, 9999)
    tasks.update({id: new_task})
    save(tasks)
    return {id:new_task}

@app.route('/addtask', methods=["POST"])
def add_task_backend():
    return_dict={}
    new_tasks=[]
    with open('addtasks.txt', 'r') as file:
        for line in file:
            new_task = line.strip()
            new_tasks.append(new_task)
    for task in new_tasks:
        id = random.randint(1000, 9999)
        tasks.update({id:task})
        return_dict.update({id:task})
        save(tasks)
    return (return_dict)

@app.route('/check', methods=["GET"])
def check():
    new_tasks=[]
    with open('check.txt', 'r') as file:
        for line in file:
            new_task = line.strip()
            new_tasks.append(new_task)
    return_dict = {}
    for id in new_tasks:
        if id in tasks:
            status_dict = {id: {"task" : tasks[id], "exists" : True}}
            return_dict.update(status_dict)
        else:
            status_dict = {id: {"task" : None , "exists" : False}}
            return_dict.update(status_dict)
    return return_dict

@app.route('/update', methods=["PUT"])
def update():
    return_dict = {}
    updates_dict = {}
    with open('update.txt', 'r') as file:
        for line in file:
            id, task = line.strip().split(",")
            updates_dict[id] = task
            print(updates_dict)
    for id, task in updates_dict.items():
        if id in tasks.keys():
            tasks.update({id : task})
            status_dict = {id: "Updated TASK " + task}
            return_dict.update(status_dict)
    save(tasks)
    return return_dict
           
@app.route('/removetask', methods=["DELETE"])
def remove_task():
    return_dict= {}
    status_dict={}
    new_tasks=[]
    with open('remove.txt', 'r') as file:
        for line in file:
            new_task = line.strip()
            new_tasks.append(new_task)
    print(new_tasks)
    print(tasks)
    for id in new_tasks:
        if id in tasks.keys():
            status_dict = {id:{"task": tasks[id], "removed" : True}}
            return_dict.update(status_dict)
            del tasks[id]
        else:
            status_dict = {id:{"task": "Does Not Exist", "removed" : False}}
            return_dict.update(status_dict)
    save(tasks)
    return return_dict



if __name__ == '__main__':
    app.run(debug=True)