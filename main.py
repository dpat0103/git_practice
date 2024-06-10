from flask import Flask, request, jsonify
global todos
todos = {}

app = Flask(__name__)


#READ/GET operation
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(todos), 200

#CREATE/POST operation
@app.route('/addtask/<task>', methods=['GET', 'POST'])
def add_task(task):
    if task in todos:
        return
    else:
        todos["id"] = task
        return jsonify(task), 200
         


if __name__ == "__main__":
    app.run(debug=True)
