// auth.js
import apiClient from './api';

export const login = async (username, password) => {
  try {
    const response = await apiClient.post('/auth/login', { username, password });
    localStorage.setItem('authToken', response.data.token);
    return response.data;
  } catch (error) {
    console.error('Login error:', error);
    throw error;
  }
};

export const logout = () => {
  localStorage.removeItem('authToken');
  window.location.href = '/login';
};

export const isAuthenticated = () => !!localStorage.getItem('authToken');
