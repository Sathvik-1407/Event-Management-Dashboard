<template>
  <div>
    <h2>Task Tracker</h2>

    <div v-if="alertMessage" :class="`alert ${alertClass}`" role="alert">
      {{ alertMessage }}
    </div>

    <div class="d-flex justify-content-between mb-3">
      <div class="dropdown">
        <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
          {{ selectedEventId ? getEventName(selectedEventId) : 'Select Event' }}
        </button>
        <ul class="dropdown-menu">
          <li v-for="event in events" :key="event.id">
            <a class="dropdown-item" href="#" @click="selectEvent(event.id)">
              {{ event.name }}
            </a>
          </li>
        </ul>
      </div>
      <button class="btn btn-primary" @click="showAddModal = true">Add Task</button>
    </div>

    <table class="table table-bordered">
      <thead>
        <tr>
          <th>Task Name</th>
          <th>Deadline</th>
          <th>Status</th>
          <th>Assigned Attendee</th>
          <th>Event</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="task in tasks" :key="task.id">
          <td>{{ task.name }}</td>
          <td>{{ task.deadline }}</td>
          <td>{{ task.status }}</td>
          <td>{{ getAttendeeName(task.assigned_attendee_id) }}</td>
          <td>{{ getEventName(task.event_id) }}</td>
          <td>
            <button class="btn btn-success btn-sm" @click="updateTaskStatus(task.id, 'Completed')">Mark as Completed</button>
            <button class="btn btn-warning btn-sm" @click="updateTaskStatus(task.id, 'Pending')">Mark as Pending</button>
          </td>
        </tr>
      </tbody>
    </table>

    <div v-if="showAddModal" class="modal" tabindex="-1" style="display:block;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add Task</h5>
            <button type="button" class="btn-close" @click="showAddModal = false"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="createTask">
              <div class="mb-3">
                <label for="name" class="form-label">Task Name</label>
                <input type="text" class="form-control" v-model="formData.name" required />
              </div>
              <div class="mb-3">
                <label for="deadline" class="form-label">Deadline</label>
                <input type="date" class="form-control" v-model="formData.deadline" required />
              </div>
              <div class="mb-3">
                <label for="assigned_attendee_id" class="form-label">Assigned Attendee</label>
                <select class="form-control" v-model="formData.assigned_attendee_id" required>
                  <option v-for="attendee in attendees" :key="attendee.id" :value="attendee.id">
                    {{ attendee.name }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label for="event_id" class="form-label">Event</label>
                <select class="form-control" v-model="formData.event_id" required>
                  <option v-for="event in events" :key="event.id" :value="event.id">
                    {{ event.name }}
                  </option>
                </select>
              </div>
              <button type="submit" class="btn btn-primary">Submit</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      tasks: [],
      attendees: [],
      events: [],
      showAddModal: false,
      formData: {
        name: "",
        deadline: "",
        assigned_attendee_id: null,
        event_id: null,
        status: "Pending",
      },
      selectedEventId: null,
      alertMessage: "",
      alertClass: "",
    };
  },
  methods: {
    selectEvent(eventId) {
      this.selectedEventId = eventId;
      this.fetchTasks(eventId);
    },
    fetchTasks(eventId) {
      this.setAlert("Fetching tasks...", "alert-info");
      axios
        .get(`http://localhost:5000/api/tasks/fetch/${eventId}`)
        .then((response) => {
          this.tasks = response.data;
          this.setAlert("Tasks fetched successfully!", "alert-success");
        })
        .catch((error) => {
          console.error("Error fetching tasks:", error);
          this.setAlert("Failed to fetch tasks.", "alert-danger");
        });
    },
    fetchAttendees() {
      axios
        .get("http://localhost:5000/api/attendee/fetch")
        .then((response) => {
          this.attendees = response.data;
        })
        .catch((error) => {
          console.error("Error fetching attendees:", error);
        });
    },
    fetchEvents() {
      axios
        .get("http://localhost:5000/api/event/fetch")
        .then((response) => {
          this.events = response.data;
        })
        .catch((error) => {
          console.error("Error fetching events:", error);
        });
    },
    createTask() {
      this.setAlert("Creating task...", "alert-info");
      axios
        .post("http://localhost:5000/api/tasks/create", this.formData)
        .then(() => {
          this.fetchTasks(this.formData.event_id);
          this.showAddModal = false;
          this.setAlert("Task created successfully!", "alert-success");
        })
        .catch((error) => {
          console.error("Error creating task:", error);
          this.setAlert("Failed to create task.", "alert-danger");
        });
    },
    updateTaskStatus(id, status) {
      this.setAlert(`Updating task status to ${status}...`, "alert-info");
      axios
        .put(`http://localhost:5000/api/tasks/update/${id}`, { status })
        .then(() => {
          this.fetchTasks(this.selectedEventId);
          this.setAlert(`Task marked as ${status}!`, "alert-success");
        })
        .catch((error) => {
          console.error("Error updating task status:", error);
          this.setAlert("Failed to update task status.", "alert-danger");
        });
    },
    getAttendeeName(attendeeId) {
      const attendee = this.attendees.find((attendee) => attendee.id === attendeeId);
      return attendee ? attendee.name : "Unknown";
    },
    getEventName(eventId) {
      const event = this.events.find((event) => event.id === eventId);
      return event ? event.name : "Unknown";
    },
    setAlert(message, alertClass) {
      this.alertMessage = message;
      this.alertClass = alertClass;
      setTimeout(() => {
        this.alertMessage = ""; 
      }, 3000);
    },
  },
  mounted() {
    this.fetchEvents();
    this.fetchAttendees();
    if (this.events.length > 0) {
      this.fetchTasks(this.events[0].id);
    }
  },
};
</script>

<style>
.modal {
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
