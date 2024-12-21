<template>
  <div>
    <h2>Attendee Management</h2>
    <button class="btn btn-primary mb-3" @click="showAddModal = true">Add Attendee</button>

    <!-- Bootstrap alert for success or error -->
    <div v-if="alertMessage" :class="`alert ${alertClass}`" role="alert">
      {{ alertMessage }}
    </div>

    <table class="table table-bordered">
      <thead>
        <tr>
          <th>Name</th>
          <th>Email</th>
          <th>Event Name</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="attendee in attendees" :key="attendee.id">
          <td>{{ attendee.name }}</td>
          <td>{{ attendee.email }}</td>
          <td>{{ attendee.event_name }}</td>
          <td>
            <button class="btn btn-danger btn-sm" @click="deleteAttendee(attendee.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <div v-if="showAddModal" class="modal" tabindex="-1" style="display:block;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add Attendee</h5>
            <button type="button" class="btn-close" @click="showAddModal = false"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="createAttendee">
              <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" v-model="formData.name" required />
              </div>
              <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" v-model="formData.email" required />
              </div>
              <div class="mb-3">
                <label for="event_id" class="form-label">Event</label>
                <select class="form-control" v-model="formData.event_id" required>
                  <option v-for="event in events" :key="event.id" :value="event.id">{{ event.name }}</option>
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
import axios from 'axios';

export default {
  data() {
    return {
      attendees: [],
      events: [],
      showAddModal: false,
      formData: {
        name: '',
        email: '',
        event_id: null
      },
      alertMessage: '',
      alertClass: ''
    };
  },
  methods: {
    fetchAttendees() {
      axios.get('http://localhost:5000/api/attendee/fetch').then(response => {
        this.attendees = response.data;
      });
    },
    fetchEvents() {
      axios.get('http://localhost:5000/api/event/fetch').then((response) => {
        this.events = response.data;
      });
    },
    createAttendee() {
      // Show info alert before starting the create operation
      this.setAlert('Creating new attendee...', 'alert-info');

      axios.post('http://localhost:5000/api/attendee/create', this.formData).then(() => {
        this.fetchAttendees();
        this.showAddModal = false;
        this.setAlert('Attendee added successfully!', 'alert-success');
      }).catch(() => {
        this.setAlert('Failed to add attendee. Please try again.', 'alert-danger');
      });
    },
    deleteAttendee(id) {
      axios.delete(`http://localhost:5000/api/attendee/delete/${id}`).then(() => {
        this.fetchAttendees();
        this.setAlert('Attendee deleted successfully!', 'alert-success');
      }).catch(() => {
        this.setAlert('Failed to delete attendee. Please try again.', 'alert-danger');
      });
    },
    showInfoAlert() {
      this.setAlert('Creating new attendee...', 'alert-info');
    },
    setAlert(message, alertClass) {
      this.alertMessage = message;
      this.alertClass = alertClass;
      setTimeout(() => {
        this.alertMessage = '';  // Hide the alert after 3 seconds
      }, 3000);
    }
  },
  mounted() {
    this.fetchAttendees();
    this.fetchEvents(); 
  }
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
