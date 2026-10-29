<template>
  <div class="flex min-h-screen bg-slate-50">
    <Sidebar />
    <div class="flex-1">
      <Navbar />
      <main class="p-8">
        <router-view></router-view>
      </main>
    </div>
  </div>
</template>

<script setup>
import Sidebar from '../components/Sidebar.vue';
import Navbar from '../components/Navbar.vue';
</script>