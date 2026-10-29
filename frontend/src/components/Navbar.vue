<template>
  <header class="h-20 bg-white border-b border-slate-200 px-8 flex items-center justify-between">
    <h2 class="text-xl font-semibold text-slate-800">{{ pageTitle }}</h2>
    <div class="flex items-center gap-4">
      <div class="text-right">
        <p class="text-sm font-bold text-slate-800">{{ auth.user?.username }}</p>
        <p class="text-xs text-slate-500">Hospital Administrator</p>
      </div>
      <div class="w-10 h-10 bg-slate-100 rounded-full flex items-center justify-center text-slate-600 font-bold">
        {{ auth.user?.username?.charAt(0).toUpperCase() }}
      </div>
    </div>
  </header>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { useAuthStore } from '../stores/auth';

const route = useRoute();
const auth = useAuthStore();

const pageTitle = computed(() => {
  if (route.path.includes('patients')) return 'Patient Management';
  if (route.path.includes('education')) return 'Education Library';
  return 'Overview';
});
</script>