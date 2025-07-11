<template>
  <div class="w-full">
    <h1 class="text-2xl font-bold text-gray-800 mb-4">Certificates</h1>
    <div class="flex flex-wrap gap-6">
      <div v-for="n in 2" :key="n" class="bg-white rounded-xl shadow p-6 flex flex-col items-center w-64">
        <font-awesome-icon :icon="['fas', 'certificate']" class="text-5xl text-green-600 mb-2" />
        <h4 class="font-bold mb-1">Certificate {{ n }}</h4>
        <p class="text-gray-500 text-sm mb-2">Course Name</p>
        <button class="px-4 py-2 rounded-xl bg-blue-600 text-white font-semibold shadow hover:bg-blue-700 transition">Download</button>
      </div>
    </div>
  </div>
</template> 