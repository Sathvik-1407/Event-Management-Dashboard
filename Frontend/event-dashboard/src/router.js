import { createRouter, createWebHistory } from 'vue-router';
import EventManagement from './components/EventManagement.vue';
import AttendeeManagement from './components/AttendeeManagement.vue';
import TaskTracker from './components/TaskTracker.vue';

const routes = [
  { path: '/', redirect: '/events' },
  { path: '/events', component: EventManagement },
  { path: '/attendees', component: AttendeeManagement },
  { path: '/tasks', component: TaskTracker }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;