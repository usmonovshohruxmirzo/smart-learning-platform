<template>
  <div class="w-full">
    <h1 class="text-2xl font-bold text-gray-800 mb-4">Instructor Dashboard</h1>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <div class="bg-white rounded-xl shadow p-6 flex flex-col items-start">
        <font-awesome-icon :icon="['fas', 'dollar-sign']" class="text-3xl text-green-600 mb-2" />
        <span class="text-lg font-semibold text-black">$1,200 Earnings</span>
      </div>
      <div class="bg-white rounded-xl shadow p-6 flex flex-col items-start">
        <font-awesome-icon :icon="['fas', 'users']" class="text-3xl text-blue-600 mb-2" />
        <span class="text-lg font-semibold text-black">320 Students</span>
      </div>
      <div class="bg-white rounded-xl shadow p-6 flex flex-col items-start">
        <font-awesome-icon :icon="['fas', 'book-open']" class="text-3xl text-purple-600 mb-2" />
        <span class="text-lg font-semibold text-black">5 Courses</span>
      </div>
    </div>
    <div class="bg-white rounded-xl shadow p-6">
      <h2 class="text-lg font-bold text-gray-800 mb-2">My Courses</h2>
      <ul class="text-gray-600 text-sm space-y-1">
        <li>Vue Mastery</li>
        <li>React Basics</li>
        <li>Advanced JS</li>
      </ul>
    </div>
  </div>
</template>
