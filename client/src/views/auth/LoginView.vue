<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const router = useRouter()

const handleLogin = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/auth/login/', {
      email: email.value,
      password: password.value,
    })
    console.log('Logged in:', response.data)
    localStorage.setItem('token', response.data.token)
    router.push('/dashboard')
  } catch (error) {
    console.error(error)
    alert('Login failed!')
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <form
      @submit.prevent="handleLogin"
      class="bg-white rounded-xl shadow p-8 w-full max-w-md flex flex-col gap-4"
    >
      <h1 class="text-2xl font-bold text-gray-800 mb-2 text-center">Sign In</h1>
      <input
        v-model="email"
        type="email"
        placeholder="Email"
        class="border border-gray-300 rounded-lg p-3"
        required
      />
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        class="border border-gray-300 rounded-lg p-3"
        required
      />
      <button
        type="submit"
        class="w-full px-4 py-2 rounded-lg bg-blue-600 text-white font-semibold hover:bg-blue-700 transition"
      >
        Login
      </button>
      <p class="text-center text-gray-500">
        <router-link to="/forgot-password/request" class="text-blue-600 hover:underline"
          >Forgot Password?</router-link
        >
      </p>
      <p class="text-center text-gray-500">
        Don't have an account?
        <router-link to="/register" class="text-blue-600 hover:underline">Register</router-link>
      </p>
    </form>
  </div>
</template>
