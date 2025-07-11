<template>
  <div class="w-full mx-auto">
    <h1 class="text-2xl font-bold text-gray-800 mb-4">Edit Course</h1>
    <div class="bg-white rounded-xl shadow p-6">
      <form class="flex flex-col gap-4">
        <input
          type="text"
          placeholder="Course Title"
          class="border border-gray-300 rounded-lg p-3"
        />
        <textarea
          placeholder="Course Description"
          class="border border-gray-300 rounded-lg p-3 resize-none"
          rows="3"
        ></textarea>
        <div>
          <label class="block font-semibold mb-1">Modules</label>
          <ul class="space-y-2 mb-2">
            <li class="flex items-center gap-2">
              <input
                type="text"
                class="border border-gray-300 rounded-lg p-2 flex-1"
                value="Introduction"
              /><button class="text-red-500 font-bold">Remove</button>
            </li>
            <li class="flex items-center gap-2">
              <input
                type="text"
                class="border border-gray-300 rounded-lg p-2 flex-1"
                value="Advanced Topics"
              /><button class="text-red-500 font-bold">Remove</button>
            </li>
          </ul>
          <button class="px-3 py-1 rounded bg-blue-100 text-blue-700 font-semibold">
            Add Module
          </button>
        </div>
        <button
          type="submit"
          class="px-4 py-2 rounded-lg bg-blue-600 text-white font-semibold hover:bg-blue-700 transition"
        >
          Save Changes
        </button>
      </form>
    </div>
  </div>
</template>
