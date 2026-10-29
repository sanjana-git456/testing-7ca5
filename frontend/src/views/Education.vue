<template>
  <div class="space-y-8">
    <div class="flex justify-between items-center">
      <h3 class="text-2xl font-bold text-slate-800">Education Library</h3>
      <div class="flex gap-2">
        <button v-for="cat in categories" :key="cat" @click="activeCat = cat" 
          :class="['px-4 py-2 rounded-lg text-sm font-medium transition', activeCat === cat ? 'bg-emerald-600 text-white' : 'bg-white text-slate-600 border border-slate-200']">
          {{ cat }}
        </button>
      </div>
    </div>

    <div v-if="isLoading" class="flex justify-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-emerald-600"></div>
    </div>

    <div v-else class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="item in filteredMaterials" :key="item.id" class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div class="aspect-video bg-slate-100">
          <iframe class="w-full h-full" :src="item.video_url" frameborder="0" allowfullscreen></iframe>
        </div>
        <div class="p-6">
          <span class="text-xs font-bold text-emerald-600 uppercase tracking-wider">{{ item.procedure_type }}</span>
          <h4 class="text-lg font-bold text-slate-800 mt-1 mb-3">{{ item.title }}</h4>
          <p class="text-slate-600 text-sm line-clamp-3">{{ item.content }}</p>
          <button class="mt-4 text-emerald-600 font-semibold text-sm hover:underline">Assign to Patient</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useQuery } from '@tanstack/vue-query';
import client from '../api/client';

const activeCat = ref('All');
const categories = ['All', 'Orthopedic', 'Cardiac', 'General'];

const { data: materials = [], isLoading } = useQuery({
  queryKey: ['education'],
  queryFn: async () => {
    const { data } = await client.get('/education/');
    return data;
  }
});

const filteredMaterials = computed(() => {
  if (activeCat.value === 'All') return materials;
  return materials.filter(m => m.procedure_type === activeCat.value);
});
</script>