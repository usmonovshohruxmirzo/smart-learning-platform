<template>
  <div class="w-full">
    <h1 class="text-2xl font-bold text-gray-800 mb-4">Welcome back, User!</h1>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <div class="bg-white rounded-xl shadow p-6 flex flex-col items-start">
        <font-awesome-icon :icon="['fas', 'book-open']" class="text-3xl text-blue-600 mb-2" />
        <span class="text-lg font-semibold text-black">4 Courses Enrolled</span>
      </div>
      <div class="bg-white rounded-xl shadow p-6 flex flex-col items-start">
        <font-awesome-icon :icon="['fas', 'certificate']" class="text-3xl text-green-600 mb-2" />
        <span class="text-lg font-semibold text-black">2 Certificates</span>
      </div>
      <div class="bg-white rounded-xl shadow p-6 flex flex-col items-start">
        <font-awesome-icon :icon="['fas', 'star']" class="text-3xl text-yellow-500 mb-2" />
        <span class="text-lg font-semibold text-black">12 Reviews</span>
      </div>
    </div>
    <div class="bg-white rounded-xl shadow p-6">
      <h2 class="text-lg font-bold text-gray-800 mb-2">Recent Activity</h2>
      <ul class="text-gray-600 text-sm space-y-1">
        <li>Completed "Vue Mastery" course</li>
        <li>Earned "Frontend Pro" certificate</li>
        <li>Left a review for "React Basics"</li>
      </ul>
    </div>
  </div>
</template>
