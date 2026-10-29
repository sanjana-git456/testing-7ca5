<template>
  <div class="space-y-6">
    <div class="flex justify-between items-center">
      <h3 class="text-2xl font-bold text-slate-800">Active Patients</h3>
      <button @click="showAddModal = true" class="bg-emerald-600 text-white px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-emerald-700 transition">
        <PlusIcon class="w-5 h-5" />
        <span>Import from FHIR</span>
      </button>
    </div>

    <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
      <table class="w-full text-left border-collapse">
        <thead class="bg-slate-50 border-b border-slate-200">
          <tr>
            <th class="px-6 py-4 text-sm font-semibold text-slate-600">Patient Name</th>
            <th class="px-6 py-4 text-sm font-semibold text-slate-600">MRN</th>
            <th class="px-6 py-4 text-sm font-semibold text-slate-600">Procedure</th>
            <th class="px-6 py-4 text-sm font-semibold text-slate-600">Risk Score</th>
            <th class="px-6 py-4 text-sm font-semibold text-slate-600">Status</th>
            <th class="px-6 py-4 text-sm font-semibold text-slate-600">Actions</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-100">
          <tr v-for="patient in patients" :key="patient.id" class="hover:bg-slate-50 transition">
            <td class="px-6 py-4 font-medium text-slate-800">{{ patient.first_name }} {{ patient.last_name }}</td>
            <td class="px-6 py-4 text-slate-500">{{ patient.mrn }}</td>
            <td class="px-6 py-4 text-slate-500">{{ patient.procedure_type }}</td>
            <td class="px-6 py-4">
              <div class="flex items-center gap-2">
                <div class="w-16 bg-slate-100 h-2 rounded-full overflow-hidden">
                  <div :class="['h-full rounded-full', patient.risk_score > 50 ? 'bg-red-500' : 'bg-emerald-500']" :style="{ width: patient.risk_score + '%' }"></div>
                </div>
                <span class="text-xs font-bold">{{ patient.risk_score }}%</span>
              </div>
            </td>
            <td class="px-6 py-4">
              <span :class="['px-2 py-1 rounded-full text-xs font-bold', patient.risk_score > 50 ? 'bg-red-50 text-red-600' : 'bg-emerald-50 text-emerald-600']">
                {{ patient.risk_score > 50 ? 'Critical' : 'Stable' }}
              </span>
            </td>
            <td class="px-6 py-4">
              <router-link :to="'/dashboard/patients/' + patient.id" class="text-emerald-600 hover:underline font-medium">View Profile</router-link>
            </td>
          </tr>
          <tr v-if="!isLoading && patients.length === 0">
            <td colspan="6" class="px-6 py-12 text-center text-slate-500">No patients found. Click "Import from FHIR" to add your first patient.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Mock Import Modal -->
    <div v-if="showAddModal" class="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-2xl p-8 max-w-md w-full">
        <h3 class="text-xl font-bold mb-4">Import Patient from FHIR</h3>
        <p class="text-slate-600 mb-6">Enter a Medical Record Number to simulate a FHIR resource import from the hospital EHR.</p>
        <input v-model="newMrn" type="text" placeholder="MRN (e.g. 12345)" class="w-full px-4 py-3 rounded-lg border border-slate-200 mb-6 outline-none focus:ring-2 focus:ring-emerald-500" />
        <div class="flex gap-3">
          <button @click="showAddModal = false" class="flex-1 px-4 py-2 border border-slate-200 rounded-lg hover:bg-slate-50">Cancel</button>
          <button @click="importPatient" class="flex-1 px-4 py-2 bg-emerald-600 text-white rounded-lg hover:bg-emerald-700">Import</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useQuery, useMutation, useQueryClient } from '@tanstack/vue-query';
import { PlusIcon } from 'lucide-vue-next';
import client from '../api/client';

const showAddModal = ref(false);
const newMrn = ref('');
const queryClient = useQueryClient();

const { data: patients = [], isLoading } = useQuery({
  queryKey: ['patients'],
  queryFn: async () => {
    const { data } = await client.get('/patients/');
    return data;
  }
});

const importMutation = useMutation({
  mutationFn: (newPatient) => client.post('/patients/', newPatient),
  onSuccess: () => {
    queryClient.invalidateQueries(['patients']);
    showAddModal.value = false;
    newMrn.value = '';
  }
});

const importPatient = () => {
  if (!newMrn.value) return;
  // Mocking FHIR data
  const mockPatient = {
    first_name: "John",
    last_name: "Doe",
    mrn: newMrn.value,
    procedure_type: "Orthopedic"
  };
  importMutation.mutate(mockPatient);
};
</script>