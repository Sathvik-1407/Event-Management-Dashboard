from flask import Blueprint, request, jsonify
from models import get_db_connection

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/api/tasks/create', methods=['POST'], endpoint='create_task')
def create_task():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (event_id, name, deadline, status, assigned_attendee_id) VALUES (%s, %s, %s, %s, %s)',
                   (data['event_id'], data['name'], data['deadline'], data['status'], data['assigned_attendee_id']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task created successfully!"}), 201

@task_bp.route('/api/tasks/fetch/<int:event_id>', methods=['GET'], endpoint='get_tasks')
def get_tasks(event_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tasks WHERE event_id=%s', (event_id,))
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)

@task_bp.route('/api/tasks/update/<int:id>', methods=['PUT'], endpoint='update_task_status')
def update_task_status(id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status=%s WHERE id=%s', (data['status'], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task updated successfully!"})
