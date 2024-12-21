<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Event Management</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/events" class="nav-link">Events</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/attendees" class="nav-link">Attendees</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/tasks" class="nav-link">Tasks</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="container mt-4">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style scoped>
body {
  min-height: 100vh;
  overflow-x: hidden;
}

.navbar {
  padding: 0.5rem 1rem;
}

.navbar-brand {
  font-size: 1.5rem;
}

@media (max-width: 767.98px) {
  .navbar-nav {
    text-align: center;
  }
}
</style>
