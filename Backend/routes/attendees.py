from flask import Blueprint, request, jsonify
from models import get_db_connection

attendee_bp = Blueprint('attendee_bp', __name__)

@attendee_bp.route('/api/attendee/create', methods=['POST'], endpoint='add_attendee')
def add_attendee():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO attendees (event_id, name, email) VALUES (%s, %s, %s)',
                   (data['event_id'], data['name'], data['email']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Attendee added successfully!"}), 201

@attendee_bp.route('/api/attendee/fetch', methods=['GET'], endpoint='get_attendees')
def get_attendees():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT attendees.id, attendees.name, attendees.email, attendees.event_id, events.name AS event_name
        FROM attendees
        JOIN events ON attendees.event_id = events.id
    ''')
    attendees = cursor.fetchall()
    conn.close()
    return jsonify(attendees)


@attendee_bp.route('/api/attendee/delete/<int:id>', methods=['DELETE'], endpoint='delete_attendee')
def delete_attendee(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM attendees WHERE id=%s', (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Attendee deleted successfully!"})
