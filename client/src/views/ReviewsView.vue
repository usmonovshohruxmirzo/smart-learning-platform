<template>
  <div class="w-full mx-auto">
    <h1 class="text-2xl font-bold text-gray-800 mb-4">Reviews</h1>
    <div class="bg-white rounded-xl shadow p-6 mb-6">
      <h2 class="text-lg font-semibold mb-2">Add a Review</h2>
      <form class="flex flex-col gap-3">
        <textarea
          class="border border-gray-300 rounded-lg p-2 resize-none"
          rows="3"
          placeholder="Write your review..."
        ></textarea>
        <div class="flex items-center gap-2">
          <span class="text-yellow-400 text-xl">★★★★★</span>
          <button
            type="submit"
            class="ml-auto px-4 py-2 rounded-lg bg-blue-600 text-white font-semibold hover:bg-blue-700 transition"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
    <div class="space-y-4">
      <div v-for="n in 3" :key="n" class="bg-white rounded-xl shadow p-4">
        <div class="flex items-center gap-2 mb-1">
          <span class="text-yellow-400">★★★★☆</span>
          <span class="text-gray-700 font-semibold">User {{ n }}</span>
        </div>
        <p class="text-gray-600 text-sm">
          This is a sample review for course {{ n }}. The platform is amazing!
        </p>
      </div>
    </div>
  </div>
</template>
