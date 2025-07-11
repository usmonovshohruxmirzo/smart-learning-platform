<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <form class="bg-white rounded-xl shadow p-8 w-full max-w-md flex flex-col gap-6">
      <h1 class="text-2xl font-bold text-gray-800 mb-2 text-center">Sign In</h1>
      <input type="email" placeholder="Email" class="border border-gray-300 rounded-lg p-3" required />
      <input type="password" placeholder="Password" class="border border-gray-300 rounded-lg p-3" required />
      <button type="submit" class="w-full px-4 py-2 rounded-lg bg-blue-600 text-white font-semibold hover:bg-blue-700 transition">Login</button>
      <p class="text-center text-gray-500">Don't have an account? <a href="/register" class="text-blue-600 hover:underline">Register</a></p>
    </form>
  </div>
</template> 