<template>
  <div class="min-h-screen bg-gray-900 text-white py-12 px-4">
    <div class="max-w-4xl mx-auto grid gap-8">
      <div class="backdrop-blur-xl bg-white/10 border border-white/20 rounded-3xl shadow-2xl p-8">
        <h1 class="text-3xl font-extrabold mb-2">Course Title</h1>
        <p class="text-lg text-gray-200 mb-4">Course subtitle and summary. <span class="inline-block bg-cyan-400/20 text-cyan-300 px-3 py-1 rounded-full ml-2 text-xs font-bold">Best Seller</span></p>
        <button class="px-8 py-3 rounded-full bg-cyan-400 text-white font-bold shadow-lg shadow-cyan-400/30 hover:scale-105 transition-transform">Enroll Now</button>
      </div>
      <div class="flex flex-col md:flex-row gap-8">
        <div class="backdrop-blur-lg bg-white/10 border border-white/20 rounded-2xl shadow-xl p-6 flex-1">
          <h2 class="text-xl font-bold mb-3">Syllabus</h2>
          <ul class="list-disc list-inside text-gray-200 space-y-1">
            <li>Module 1: Introduction</li>
            <li>Module 2: Advanced Topics</li>
            <li>Module 3: Project</li>
          </ul>
        </div>
        <div class="backdrop-blur-lg bg-white/10 border border-white/20 rounded-2xl shadow-xl p-6 flex-1 flex flex-col items-center">
          <h2 class="text-xl font-bold mb-3">Instructor</h2>
          <img class="w-20 h-20 rounded-full border-4 border-cyan-400 mb-2" src="https://randomuser.me/api/portraits/men/32.jpg" alt="Instructor" />
          <div class="text-center">
            <h3 class="font-semibold">John Doe</h3>
            <p class="text-gray-400">Lead Instructor</p>
          </div>
        </div>
      </div>
      <div class="backdrop-blur-lg bg-white/10 border border-white/20 rounded-2xl shadow-xl p-6">
        <h2 class="text-xl font-bold mb-3">Reviews</h2>
        <div class="flex items-center gap-2 mb-2">
          <span class="text-yellow-400 text-lg">★ ★ ★ ★ ☆</span>
          <span class="text-gray-400 text-sm">4.0 (120 reviews)</span>
        </div>
        <div class="space-y-2">
          <p><b>Jane:</b> Amazing course!</p>
          <p><b>Alex:</b> Loved the content and style.</p>
        </div>
      </div>
    </div>
  </div>
</template> 