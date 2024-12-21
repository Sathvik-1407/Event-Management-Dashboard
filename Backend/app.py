from flask import Flask
from flask_cors import CORS
from routes.events import event_bp
from routes.attendees import attendee_bp
from routes.tasks import task_bp

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

app.register_blueprint(event_bp)
app.register_blueprint(attendee_bp)
app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(debug=True)
