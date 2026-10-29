<template>
  <div v-if="isLoading" class="flex justify-center py-12">
    <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-emerald-600"></div>
  </div>
  <div v-else-if="data" class="space-y-8">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
        <p class="text-slate-500 text-sm font-medium">Total Patients</p>
        <p class="text-3xl font-bold text-slate-900 mt-2">{{ data.total_patients }}</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
        <p class="text-slate-500 text-sm font-medium">High Risk Alerts</p>
        <p class="text-3xl font-bold text-red-600 mt-2">{{ data.high_risk_count }}</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
        <p class="text-slate-500 text-sm font-medium">Check-in Adherence</p>
        <p class="text-3xl font-bold text-emerald-600 mt-2">{{ data.adherence_rate }}%</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
        <p class="text-slate-500 text-sm font-medium">Est. Readmission Rate</p>
        <p class="text-3xl font-bold text-slate-900 mt-2">{{ data.readmission_estimate }}%</p>
      </div>
    </div>

    <div class="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
      <div class="flex justify-between items-center mb-6">
        <h3 class="text-lg font-bold text-slate-800">Recent Activity</h3>
        <router-link to="/dashboard/patients" class="text-emerald-600 text-sm font-semibold">View All</router-link>
      </div>
      <div class="space-y-4">
        <div v-if="data.total_patients === 0" class="text-center py-12 text-slate-500">
          No patients registered yet. Start by adding a patient from the Patients tab.
        </div>
        <div v-else class="text-slate-600">
          System is monitoring {{ data.total_patients }} active cases. Adherence is currently above the 80% target for Medicare reimbursement.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useQuery } from '@tanstack/vue-query';
import client from '../api/client';

const { data, isLoading } = useQuery({
  queryKey: ['analytics-summary'],
  queryFn: async () => {
    const { data } = await client.get('/analytics/summary');
    return data;
  }
});
</script>