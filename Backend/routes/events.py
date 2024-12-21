from flask import Blueprint, request, jsonify
from models import get_db_connection

event_bp = Blueprint('event_bp', __name__)

@event_bp.route('/api/event/create', methods=['POST'], endpoint='create_event')
def create_event():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO events (name, description, location, event_date) VALUES (%s, %s, %s, %s)',
                   (data['name'], data['description'], data['location'], data['event_date']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Event created successfully!"}), 201

@event_bp.route('/api/event/fetch', methods=['GET'], endpoint='get_events')
def get_events():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM events')
    events = cursor.fetchall()
    conn.close()
    return jsonify(events)

@event_bp.route('/api/event/update/<int:id>', methods=['PUT'], endpoint='update_event')
def update_event(id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE events SET name=%s, description=%s, location=%s, event_date=%s WHERE id=%s',
                   (data['name'], data['description'], data['location'], data['event_date'], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Event updated successfully!"})

@event_bp.route('/api/event/delete/<int:id>', methods=['DELETE'], endpoint='delete_event')
def delete_event(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM events WHERE id=%s', (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Event deleted successfully!"})
