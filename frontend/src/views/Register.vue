<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-emerald-500 to-teal-700 p-4">
    <div class="bg-white p-8 rounded-2xl shadow-2xl w-full max-w-md">
      <div class="text-center mb-8">
        <h2 class="text-3xl font-bold text-slate-800">Create Account</h2>
        <p class="text-slate-500 mt-2">Join DischargeGuard hospital network</p>
      </div>

      <form @submit.prevent="handleRegister" class="space-y-6">
        <div v-if="error" class="p-3 bg-red-50 text-red-600 rounded-lg text-sm">
          {{ error }}
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Username</label>
          <input v-model="form.username" type="text" required class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:ring-2 focus:ring-emerald-500 outline-none transition" />
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Email Address</label>
          <input v-model="form.email" type="email" required class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:ring-2 focus:ring-emerald-500 outline-none transition" />
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Password</label>
          <input v-model="form.password" type="password" required class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:ring-2 focus:ring-emerald-500 outline-none transition" />
        </div>
        <button :disabled="loading" type="submit" class="w-full bg-emerald-600 text-white py-3 rounded-lg font-semibold hover:bg-emerald-700 transition disabled:opacity-50">
          {{ loading ? 'Creating Account...' : 'Register' }}
        </button>
      </form>

      <div class="mt-6 text-center text-sm text-slate-600">
        Already have an account? <router-link to="/login" class="text-emerald-600 font-semibold">Log In</router-link>
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
const form = reactive({ username: '', email: '', password: '' });
const loading = ref(false);
const error = ref('');

const handleRegister = async () => {
  loading.value = true;
  error.value = '';
  try {
    await auth.register(form.username, form.email, form.password);
    router.push('/dashboard');
  } catch (err) {
    error.value = err.response?.data?.detail || 'Registration failed';
  } finally {
    loading.value = false;
  }
};
</script>