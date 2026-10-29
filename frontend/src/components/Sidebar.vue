<template>
  <aside class="w-64 bg-white border-r border-slate-200 flex flex-col">
    <div class="p-6 flex items-center gap-3">
      <div class="w-8 h-8 bg-emerald-600 rounded-lg flex items-center justify-center text-white">
        <ShieldCheckIcon class="w-5 h-5" />
      </div>
      <span class="font-bold text-xl text-slate-800">DischargeGuard</span>
    </div>

    <nav class="flex-1 px-4 space-y-2">
      <router-link to="/dashboard" exact-active-class="bg-emerald-50 text-emerald-600" class="flex items-center gap-3 px-4 py-3 rounded-lg text-slate-600 hover:bg-slate-50 transition">
        <LayoutDashboardIcon class="w-5 h-5" />
        <span>Dashboard</span>
      </router-link>
      <router-link to="/dashboard/patients" active-class="bg-emerald-50 text-emerald-600" class="flex items-center gap-3 px-4 py-3 rounded-lg text-slate-600 hover:bg-slate-50 transition">
        <UsersIcon class="w-5 h-5" />
        <span>Patients</span>
      </router-link>
      <router-link to="/dashboard/education" active-class="bg-emerald-50 text-emerald-600" class="flex items-center gap-3 px-4 py-3 rounded-lg text-slate-600 hover:bg-slate-50 transition">
        <BookOpenIcon class="w-5 h-5" />
        <span>Education</span>
      </router-link>
    </nav>

    <div class="p-4 border-t border-slate-200">
      <button @click="logout" class="flex items-center gap-3 px-4 py-3 w-full text-left text-slate-600 hover:bg-red-50 hover:text-red-600 rounded-lg transition">
        <LogOutIcon class="w-5 h-5" />
        <span>Logout</span>
      </button>
    </div>
  </aside>
</template>

<script setup>
import { ShieldCheckIcon, LayoutDashboardIcon, UsersIcon, BookOpenIcon, LogOutIcon } from 'lucide-vue-next';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();

const logout = () => {
  auth.logout();
  router.push('/');
};
</script>