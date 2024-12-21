# Backend README

## Overview

This backend is built to support a Task Tracker application, providing APIs for managing tasks, attendees, and events. It is developed using Flask, a lightweight Python web framework, and uses a RESTful architecture for communication with the frontend.

---

## Features

- **Task Management**: Create, update, and fetch tasks with assigned attendees and deadlines.
- **Event Management**: Manage events, including creating, updating, and deleting events.
- **Attendee Management**: Handle attendee records and assign them to tasks.

---

## Technologies Used

- **Framework**: Flask
- **Database**: SQLite (default) or any SQL database compatible with SQLAlchemy
- **HTTP Client**: Flask-RESTful for API endpoints
- **CORS Handling**: Flask-CORS

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sathvik-1407/Event-Management-Dashboard.git
   cd Backend
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r Requirements.txt
   ```

4. Start the server:

   ```bash
   python app.py
   ```

5. The server will run at `http://localhost:5000` by default.

---

## API Endpoints

### Tasks

- GET /api/tasks/fetch/:eventId**     : Fetch tasks for a specific event.
- POST /api/tasks/create              : Create a new task.
- PUT /api/tasks/update/:taskId**     : Update the status of a task.

### Events

- GET /api/event/fetch              : Fetch all events.
- POST /api/event/create            : Create a new event.
- PUT /api/event/update/:eventId    : Update an event.
- DELETE /api/event/delete/:eventId : Delete an event.

### Attendees

- GET /api/attendee/fetch             : Fetch all attendees.
- POST /api/tasks/create              : Create a new task by providing the task details.
- DELETE /api/tasks/delete/:attedeeId : Delete a specific task using its task ID.

---

## Error Handling

- All API responses include a status code and a message.
- Common errors include:
  - `400 Bad Request`: Invalid input.
  - `404 Not Found`: Resource not found.
  - `500 Internal Server Error`: Unexpected server error.

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

For questions or support, please contact:

- Name: N A Sathvik
- Email: sathviknanikeri000\@gmail.com

