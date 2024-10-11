from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        task = request.json
        task['id'] = len(tasks) + 1
        tasks.append(task)
        return jsonify(task), 201
    else:
        return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
