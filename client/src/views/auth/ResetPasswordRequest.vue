<script setup lang="ts">
import { ref } from 'vue'

const email = ref<string>('')

const handleResetPassword = async () => {}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <form
      @submit.prevent="handleResetPassword"
      class="bg-white rounded-xl shadow p-8 w-full max-w-md flex flex-col gap-4"
    >
      <h1 class="text-2xl font-bold text-gray-800 mb-2 text-center">Reset Password Request</h1>
      <input
        v-model="email"
        type="email"
        placeholder="Email"
        class="border border-gray-300 rounded-lg p-3"
        required
      />
      <button
        type="submit"
        class="w-full px-4 py-2 rounded-lg bg-blue-600 text-white font-semibold hover:bg-blue-700 transition"
      >
        Submit
      </button>
    </form>
  </div>
</template>
