import { defineStore } from 'pinia';
import client from '../api/client';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('user')) || null,
    token: localStorage.getItem('token') || null,
  }),
  getters: {
    isAuthenticated: (state) => !!state.token,
  },
  actions: {
    async login(username, password) {
      const { data } = await client.post('/auth/login', { username, password });
      this.token = data.access;
      this.user = data.user;
      localStorage.setItem('token', data.access);
      localStorage.setItem('user', JSON.stringify(data.user));
    },
    async register(username, email, password) {
      const { data } = await client.post('/auth/register', { username, email, password });
      this.token = data.access;
      this.user = data.user;
      localStorage.setItem('token', data.access);
      localStorage.setItem('user', JSON.stringify(data.user));
    },
    logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem('token');
      localStorage.removeItem('user');
    }
  }
});