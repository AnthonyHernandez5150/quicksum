<template>
  <div class="dashboard-layout">
    <header>
      <h1>Dashboard</h1>
      <nav>
        <router-link to="/dashboard">Home</router-link>
        <router-link to="/profile">Profile</router-link>
        <router-link to="/settings">Settings</router-link>
        <router-link to="/logout">Logout</router-link>
      </nav>
    </header>
    <main>
      <slot></slot>
    </main>
    <footer>
      <p>&copy; 2023 Your Company</p>
    </footer>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'DashboardLayout',
});
</script>

<style scoped>
.dashboard-layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

header {
  background-color: #f8f9fa;
  padding: 1rem;
  border-bottom: 1px solid #dee2e6;
}

nav {
  margin-top: 1rem;
}

nav a {
  margin-right: 1rem;
  text-decoration: none;
  color: #007bff;
}

main {
  flex: 1;
  padding: 1rem;
}

footer {
  background-color: #f8f9fa;
  padding: 1rem;
  text-align: center;
}
</style>