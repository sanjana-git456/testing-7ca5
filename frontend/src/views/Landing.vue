<template>
  <div class="min-h-screen bg-white">
    <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex justify-between items-center">
      <div class="flex items-center gap-2">
        <div class="w-10 h-10 bg-emerald-600 rounded-xl flex items-center justify-center text-white">
          <ShieldCheckIcon class="w-6 h-6" />
        </div>
        <span class="text-2xl font-bold text-slate-900">DischargeGuard</span>
      </div>
      <div class="flex gap-4">
        <router-link to="/login" class="text-slate-600 hover:text-emerald-600 font-medium">Log in</router-link>
        <router-link to="/register" class="bg-emerald-600 text-white px-5 py-2 rounded-lg font-medium hover:bg-emerald-700">Get Started</router-link>
      </div>
    </nav>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 pb-32">
      <div class="text-center max-w-3xl mx-auto">
        <h1 class="text-5xl font-extrabold text-slate-900 tracking-tight mb-6">
          Reduce Readmissions with <span class="text-emerald-600">Intelligent Post-Discharge Care</span>
        </h1>
        <p class="text-xl text-slate-600 mb-10">
          Automated symptom monitoring, FHIR-integrated education, and smart scheduling to keep patients safe after they leave the hospital.
        </p>
        <div class="flex justify-center gap-4">
          <router-link to="/register" class="bg-emerald-600 text-white px-8 py-4 rounded-xl text-lg font-semibold hover:bg-emerald-700 shadow-lg">Start Monitoring Now</router-link>
        </div>
      </div>

      <div class="mt-32 grid md:grid-cols-3 gap-12">
        <div class="p-8 rounded-2xl bg-slate-50 border border-slate-100">
          <div class="w-12 h-12 bg-emerald-100 text-emerald-600 rounded-lg flex items-center justify-center mb-6">
            <ActivityIcon class="w-6 h-6" />
          </div>
          <h3 class="text-xl font-bold mb-3">Daily Check-ins</h3>
          <p class="text-slate-600">Automated symptom prompts detect complications early, alerting clinical teams before readmission is necessary.</p>
        </div>
        <div class="p-8 rounded-2xl bg-slate-50 border border-slate-100">
          <div class="w-12 h-12 bg-emerald-100 text-emerald-600 rounded-lg flex items-center justify-center mb-6">
            <CalendarIcon class="w-6 h-6" />
          </div>
          <h3 class="text-xl font-bold mb-3">Smart Scheduling</h3>
          <p class="text-slate-600">Follow-up appointments are automatically prioritized based on patient risk scores and procedure complexity.</p>
        </div>
        <div class="p-8 rounded-2xl bg-slate-50 border border-slate-100">
          <div class="w-12 h-12 bg-emerald-100 text-emerald-600 rounded-lg flex items-center justify-center mb-6">
            <BookOpenIcon class="w-6 h-6" />
          </div>
          <h3 class="text-xl font-bold mb-3">Tailored Education</h3>
          <p class="text-slate-600">Patients receive procedure-specific video libraries and instructions via FHIR integration.</p>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ShieldCheckIcon, ActivityIcon, CalendarIcon, BookOpenIcon } from 'lucide-vue-next';
</script>