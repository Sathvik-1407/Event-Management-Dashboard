<template>
  <div>
    <h2>Event Management</h2>
    <button class="btn btn-primary mb-3" @click="showAddModal = true">Add Event</button>
    
    <div v-if="alertMessage" :class="`alert ${alertClass}`" role="alert">
      {{ alertMessage }}
    </div>

    <table class="table table-bordered">
      <thead>
        <tr>
          <th>Name</th>
          <th>Description</th>
          <th>Location</th>
          <th>Date</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="event in events" :key="event.id">
          <td>{{ event.name }}</td>
          <td>{{ event.description }}</td>
          <td>{{ event.location }}</td>
          <td>{{ event.event_date }}</td>
          <td>
            <button class="btn btn-success btn-sm" @click="editEvent(event)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="deleteEvent(event.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <div v-if="showAddModal" class="modal" tabindex="-1" style="display:block;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ editMode ? 'Edit Event' : 'Add Event' }}</h5>
            <button type="button" class="btn-close" @click="showAddModal = false"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="editMode ? updateEvent() : createEvent()">
              <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" v-model="formData.name" required />
              </div>
              <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea class="form-control" v-model="formData.description" required></textarea>
              </div>
              <div class="mb-3">
                <label for="location" class="form-label">Location</label>
                <input type="text" class="form-control" v-model="formData.location" required />
              </div>
              <div class="mb-3">
                <label for="date" class="form-label">Date</label>
                <input type="date" class="form-control" v-model="formData.event_date" required />
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
      events: [],
      showAddModal: false,
      editMode: false,
      formData: {
        id: null,
        name: '',
        description: '',
        location: '',
        event_date: ''
      },
      alertMessage: '',
      alertClass: ''
    };
  },
  methods: {
    fetchEvents() {
      axios.get('http://localhost:5000/api/event/fetch').then(response => {
        this.events = response.data;
      });
    },
    createEvent() {
      this.setAlert('Creating new event...', 'alert-info');

      axios.post('http://localhost:5000/api/event/create', this.formData).then(() => {
        this.fetchEvents();
        this.showAddModal = false;
        this.setAlert('Event created successfully!', 'alert-success');
      }).catch(() => {
        this.setAlert('Failed to create event. Please try again.', 'alert-danger');
      });
    },
    editEvent(event) {
      this.formData = { ...event };
      this.editMode = true;
      this.showAddModal = true;
    },
    updateEvent() {
      this.setAlert('Updating event...', 'alert-info');

      axios.put(`http://localhost:5000/api/event/update/${this.formData.id}`, this.formData).then(() => {
        this.fetchEvents();
        this.showAddModal = false;
        this.editMode = false;
        this.setAlert('Event updated successfully!', 'alert-success');
      }).catch(() => {
        this.setAlert('Failed to update event. Please try again.', 'alert-danger');
      });
    },
    deleteEvent(id) {
      this.setAlert('Deleting event...', 'alert-info');

      axios.delete(`http://localhost:5000/api/event/delete/${id}`).then(() => {
        this.fetchEvents();
        this.setAlert('Event deleted successfully!', 'alert-success');
      }).catch(() => {
        this.setAlert('Failed to delete event. Please try again.', 'alert-danger');
      });
    },
    setAlert(message, alertClass) {
      this.alertMessage = message;
      this.alertClass = alertClass;
      setTimeout(() => {
        this.alertMessage = '';
      }, 3000);
    }
  },
  mounted() {
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
