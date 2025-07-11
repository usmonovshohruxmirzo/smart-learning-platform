<template>
  <div class="w-full">
    <h1 class="text-2xl font-bold text-gray-800 mb-4">My Courses</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="n in 6" :key="n" class="bg-white rounded-xl shadow p-6 flex flex-col">
        <h3 class="font-semibold text-blue-700 mb-1">Course {{ n }}</h3>
        <p class="text-gray-500 text-sm mb-2">Short description of course {{ n }}.</p>
        <button class="mt-auto px-4 py-2 rounded-lg bg-blue-600 text-white font-semibold hover:bg-blue-700 transition">Continue</button>
      </div>
    </div>
  </div>
</template> 