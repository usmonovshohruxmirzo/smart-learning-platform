<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const fullName = ref('')
const email = ref('')
const password = ref('')
const bio = ref('')
const phoneNumber = ref('')
const avatar = ref(null)

const router = useRouter()

const handleRegister = async () => {
  const formData = new FormData()
  formData.append('full_name', fullName.value)
  formData.append('email', email.value)
  formData.append('password', password.value)
  formData.append('bio', bio.value)
  formData.append('phone_number', phoneNumber.value)
  if (avatar.value) {
    formData.append('avatar', avatar.value)
  }

  try {
    const response = await axios.post('http://127.0.0.1:8000/api/auth/register/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    console.log('Registered:', response.data)
    router.push('/login')
  } catch (error) {
    console.error(error)
    alert('Registration failed!')
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <form
      @submit.prevent="handleRegister"
      class="bg-white rounded-xl shadow p-8 w-full max-w-md flex flex-col gap-4"
    >
      <h1 class="text-2xl font-bold text-gray-800 mb-2 text-center">Create Account</h1>
      <input
        v-model="fullName"
        type="text"
        placeholder="Full Name"
        class="border border-gray-300 rounded-lg p-3 text-black"
        required
      />
      <input
        v-model="email"
        type="email"
        placeholder="Email"
        class="border border-gray-300 rounded-lg p-3 text-black"
        required
      />
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        class="border border-gray-300 rounded-lg p-3 text-black"
        required
      />
      <input
        @change="(e) => (avatar.value = e.target.files[0])"
        type="file"
        class="border border-gray-300 rounded-lg p-3 text-black"
      />
      <button
        type="submit"
        class="w-full px-4 py-2 rounded-lg bg-blue-600 text-white font-semibold hover:bg-blue-700 transition"
      >
        Register
      </button>
      <p class="text-center text-gray-500">
        Already have an account? <a href="/login" class="text-blue-600 hover:underline">Login</a>
      </p>
    </form>
  </div>
</template>
