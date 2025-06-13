<template>
  <DashboardLayout>
    <h1>Welcome to Your Dashboard</h1>
    <p>This is the main dashboard view where you can access your notes and other features.</p>
    <!-- Additional dashboard content can be added here -->
  </DashboardLayout>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Dashboard',
});
</script>

<style scoped>
h1 {
  color: #333;
}

p {
  font-size: 1.2em;
}
</style>