<template>
  <div class="w-full mx-auto">
    <h1 class="text-2xl font-bold text-gray-800 mb-4">Assignments / Tasks</h1>
    <div class="bg-white rounded-xl shadow p-6 space-y-4">
      <div class="flex items-center gap-3">
        <input type="checkbox" checked class="accent-blue-600" />
        <span class="font-semibold text-gray-700">Finish Vue project</span>
        <span class="ml-auto text-xs text-gray-400">Due: Today</span>
      </div>
      <div class="flex items-center gap-3">
        <input type="checkbox" class="accent-blue-600" />
        <span class="font-semibold text-gray-700">Read React docs</span>
        <span class="ml-auto text-xs text-gray-400">Due: Tomorrow</span>
      </div>
      <div class="flex items-center gap-3">
        <input type="checkbox" class="accent-blue-600" />
        <span class="font-semibold text-gray-700">Submit assignment</span>
        <span class="ml-auto text-xs text-gray-400">Due: Friday</span>
      </div>
    </div>
  </div>
</template> 