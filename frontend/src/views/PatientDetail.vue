<template>
  <div v-if="isLoading" class="flex justify-center py-12">
    <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-emerald-600"></div>
  </div>
  <div v-else-if="patient" class="space-y-8">
    <div class="flex items-center gap-4">
      <router-link to="/dashboard/patients" class="p-2 hover:bg-slate-100 rounded-lg">
        <ChevronLeftIcon class="w-6 h-6 text-slate-600" />
      </router-link>
      <h2 class="text-2xl font-bold text-slate-800">{{ patient.first_name }} {{ patient.last_name }}</h2>
      <span :class="['px-3 py-1 rounded-full text-sm font-bold', patient.risk_score > 50 ? 'bg-red-100 text-red-600' : 'bg-emerald-100 text-emerald-600']">
        Risk Score: {{ patient.risk_score }}%
      </span>
    </div>

    <div class="grid md:grid-cols-3 gap-8">
      <div class="md:col-span-2 space-y-8">
        <div class="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
          <h3 class="text-lg font-bold mb-6">Check-in History</h3>
          <div v-if="patient.checkins.length === 0" class="text-center py-12 text-slate-500">
            No check-ins recorded yet.
          </div>
          <div v-else class="space-y-4">
            <div v-for="checkin in patient.checkins" :key="checkin.id" class="p-4 border border-slate-100 rounded-xl">
              <div class="flex justify-between mb-2">
                <span class="font-bold">{{ new Date(checkin.timestamp).toLocaleDateString() }}</span>
                <span class="text-slate-500 text-sm">{{ new Date(checkin.timestamp).toLocaleTimeString() }}</span>
              </div>
              <div class="grid grid-cols-2 gap-4 text-sm">
                <div><span class="text-slate-500">Pain Level:</span> {{ checkin.pain_level }}/10</div>
                <div><span class="text-slate-500">Temp:</span> {{ checkin.temperature }}°C</div>
                <div><span class="text-slate-500">Redness:</span> {{ checkin.redness ? 'Yes' : 'No' }}</div>
                <div><span class="text-slate-500">Shortness of Breath:</span> {{ checkin.shortness_of_breath ? 'Yes' : 'No' }}</div>
              </div>
            </div>
          </div>
          <button @click="showCheckinModal = true" class="mt-6 w-full py-2 bg-slate-50 text-slate-600 rounded-lg border border-dashed border-slate-300 hover:bg-slate-100 transition">
            + Add Manual Check-in
          </button>
        </div>
      </div>

      <div class="space-y-8">
        <div class="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
          <h3 class="text-lg font-bold mb-4">Patient Info</h3>
          <div class="space-y-3 text-sm">
            <div class="flex justify-between">
              <span class="text-slate-500">MRN</span>
              <span class="font-medium">{{ patient.mrn }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-500">Discharged</span>
              <span class="font-medium">{{ new Date(patient.discharge_date).toLocaleDateString() }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-500">Procedure</span>
              <span class="font-medium">{{ patient.procedure_type }}</span>
            </div>
          </div>
        </div>

        <div class="bg-emerald-600 p-8 rounded-2xl shadow-lg text-white">
          <h3 class="text-lg font-bold mb-4">Smart Scheduling</h3>
          <p class="text-emerald-100 text-sm mb-6">Based on the risk score, the next follow-up is recommended within 48 hours.</p>
          <button class="w-full bg-white text-emerald-600 py-2 rounded-lg font-bold hover:bg-emerald-50 transition">
            Schedule Follow-up
          </button>
        </div>
      </div>
    </div>

    <!-- Manual Check-in Modal -->
    <div v-if="showCheckinModal" class="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-2xl p-8 max-w-md w-full">
        <h3 class="text-xl font-bold mb-4">Record Check-in</h3>
        <form @submit.prevent="submitCheckin" class="space-y-4">
          <div>
            <label class="block text-sm font-medium mb-1">Pain Level (1-10)</label>
            <input v-model="checkinForm.pain_level" type="number" min="1" max="10" class="w-full px-4 py-2 border rounded-lg" />
          </div>
          <div>
            <label class="block text-sm font-medium mb-1">Temperature (°C)</label>
            <input v-model="checkinForm.temperature" type="number" step="0.1" class="w-full px-4 py-2 border rounded-lg" />
          </div>
          <div class="flex gap-4">
            <label class="flex items-center gap-2">
              <input v-model="checkinForm.redness" type="checkbox" /> Redness?
            </label>
            <label class="flex items-center gap-2">
              <input v-model="checkinForm.shortness_of_breath" type="checkbox" /> SOB?
            </label>
          </div>
          <div class="flex gap-3 pt-4">
            <button type="button" @click="showCheckinModal = false" class="flex-1 px-4 py-2 border rounded-lg">Cancel</button>
            <button type="submit" class="flex-1 px-4 py-2 bg-emerald-600 text-white rounded-lg">Save</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRoute } from 'vue-router';
import { useQuery, useMutation, useQueryClient } from '@tanstack/vue-query';
import { ChevronLeftIcon } from 'lucide-vue-next';
import client from '../api/client';

const route = useRoute();
const queryClient = useQueryClient();
const showCheckinModal = ref(false);
const checkinForm = reactive({
  pain_level: 1,
  temperature: 36.6,
  redness: false,
  shortness_of_breath: false
});

const { data: patient, isLoading } = useQuery({
  queryKey: ['patient', route.params.id],
  queryFn: async () => {
    const { data } = await client.get(`/patients/${route.params.id}`);
    return data;
  }
});

const checkinMutation = useMutation({
  mutationFn: (payload) => client.post('/checkins/', payload),
  onSuccess: () => {
    queryClient.invalidateQueries(['patient', route.params.id]);
    showCheckinModal.value = false;
  }
});

const submitCheckin = () => {
  checkinMutation.mutate({
    ...checkinForm,
    patient_id: parseInt(route.params.id)
  });
};
</script>