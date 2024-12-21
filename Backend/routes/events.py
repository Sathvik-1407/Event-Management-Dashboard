from flask import Blueprint, request, jsonify
from models import get_db_connection
from mysql.connector import Error

event_bp = Blueprint('event_bp', __name__)

@event_bp.route('/api/event/create', methods=['POST'], endpoint='create_event')
def create_event():
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO events (name, description, location, event_date) VALUES (%s, %s, %s, %s)',
                       (data['name'], data['description'], data['location'], data['event_date']))
        conn.commit()
        return jsonify({"message": "Event created successfully!"}), 201
    except Error as e:
        return jsonify({"error": "Failed to create event", "details": str(e)}), 500
    finally:
        if conn:
            conn.close()

@event_bp.route('/api/event/fetch', methods=['GET'], endpoint='get_events')
def get_events():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM events')
        events = cursor.fetchall()
        return jsonify(events)
    except Error as e:
        return jsonify({"error": "Failed to fetch events", "details": str(e)}), 500
    finally:
        if conn:
            conn.close()

@event_bp.route('/api/event/update/<int:id>', methods=['PUT'], endpoint='update_event')
def update_event(id):
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE events SET name=%s, description=%s, location=%s, event_date=%s WHERE id=%s',
                       (data['name'], data['description'], data['location'], data['event_date'], id))
        conn.commit()
        return jsonify({"message": "Event updated successfully!"})
    except Error as e:
        return jsonify({"error": "Failed to update event", "details": str(e)}), 500
    finally:
        if conn:
            conn.close()

@event_bp.route('/api/event/delete/<int:id>', methods=['DELETE'], endpoint='delete_event')
def delete_event(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM events WHERE id=%s', (id,))
        conn.commit()
        return jsonify({"message": "Event deleted successfully!"})
    except Error as e:
        return jsonify({"error": "Failed to delete event", "details": str(e)}), 500
    finally:
        if conn:
            conn.close()
