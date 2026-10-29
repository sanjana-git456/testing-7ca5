<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-emerald-500 to-teal-700 p-4">
    <div class="bg-white p-8 rounded-2xl shadow-2xl w-full max-w-md">
      <div class="text-center mb-8">
        <h2 class="text-3xl font-bold text-slate-800">Welcome Back</h2>
        <p class="text-slate-500 mt-2">Log in to manage your patients</p>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-6">
        <div v-if="error" class="p-3 bg-red-50 text-red-600 rounded-lg text-sm">
          {{ error }}
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Username</label>
          <input v-model="form.username" type="text" required class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:ring-2 focus:ring-emerald-500 outline-none transition" placeholder="Enter your username" />
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Password</label>
          <input v-model="form.password" type="password" required class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:ring-2 focus:ring-emerald-500 outline-none transition" placeholder="••••••••" />
        </div>
        <button :disabled="loading" type="submit" class="w-full bg-emerald-600 text-white py-3 rounded-lg font-semibold hover:bg-emerald-700 transition disabled:opacity-50">
          {{ loading ? 'Logging in...' : 'Log In' }}
        </button>
      </form>

      <div class="mt-6 text-center text-sm text-slate-600">
        Don't have an account? <router-link to="/register" class="text-emerald-600 font-semibold">Register</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';

const router = useRouter();
const auth = useAuthStore();
const form = reactive({ username: '', password: '' });
const loading = ref(false);
const error = ref('');

const handleLogin = async () => {
  loading.value = true;
  error.value = '';
  try {
    await auth.login(form.username, form.password);
    router.push('/dashboard');
  } catch (err) {
    error.value = err.response?.data?.detail || 'Login failed';
  } finally {
    loading.value = false;
  }
};
</script>