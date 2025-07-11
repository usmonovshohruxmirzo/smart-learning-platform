<template>
  <div class="w-full py-12 px-4 bg-gray-100 min-h-screen">
    <div class="mx-auto grid gap-8">
      <div class="bg-white rounded-xl shadow p-8">
        <h1 class="text-3xl font-extrabold text-gray-900 mb-2">Course Title</h1>
        <p class="text-lg text-gray-700 mb-4">
          Course subtitle and summary.
          <span class="inline-block bg-blue-100 text-blue-700 px-3 py-1 rounded-full ml-2 text-xs font-bold">Best Seller</span>
        </p>
        <button class="px-8 py-3 rounded-lg bg-blue-600 text-white font-bold shadow hover:bg-blue-700 transition-transform">Enroll Now</button>
      </div>
      <div class="flex flex-col md:flex-row gap-8">
        <div class="bg-white rounded-xl shadow p-6 flex-1">
          <h2 class="text-xl font-bold text-gray-900 mb-3">Syllabus</h2>
          <ul class="list-disc list-inside text-gray-700 space-y-1">
            <li>Module 1: Introduction</li>
            <li>Module 2: Advanced Topics</li>
            <li>Module 3: Project</li>
          </ul>
        </div>
        <div class="bg-white rounded-xl shadow p-6 flex-1 flex flex-col items-center">
          <h2 class="text-xl font-bold text-gray-900 mb-3">Instructor</h2>
          <img class="w-20 h-20 rounded-full border-4 border-blue-400 mb-2" src="https://randomuser.me/api/portraits/men/32.jpg" alt="Instructor" />
          <div class="text-center">
            <h3 class="font-semibold text-gray-900">John Doe</h3>
            <p class="text-gray-500">Lead Instructor</p>
          </div>
        </div>
      </div>
      <div class="bg-white rounded-xl shadow p-6">
        <h2 class="text-xl font-bold text-gray-900 mb-3">Reviews</h2>
        <div class="flex items-center gap-2 mb-2">
          <span class="text-yellow-400 text-lg">★ ★ ★ ★ ☆</span>
          <span class="text-gray-500 text-sm">4.0 (120 reviews)</span>
        </div>
        <div class="space-y-2">
          <p class="text-black"><b>Jane:</b> Amazing course!</p>
          <p class="text-black"><b>Alex:</b> Loved the content and style.</p>
        </div>
      </div>
    </div>
  </div>
</template> 