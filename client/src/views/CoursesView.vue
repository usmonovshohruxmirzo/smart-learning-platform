<template>
  <div class="w-full">
    <h1 class="text-2xl font-bold text-gray-800 mb-4">My Courses</h1>

    <div v-if="loading" class="text-center text-gray-500">Loading courses...</div>
    <div v-else-if="error" class="text-center text-red-500">{{ error }}</div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div
        v-for="course in courses"
        :key="course.id"
        class="bg-white rounded-xl shadow p-6 flex flex-col"
      >
        <h3 class="font-semibold text-blue-700 mb-1">{{ course.title }}</h3>
        <p class="text-gray-500 text-sm mb-2">{{ course.description || 'No description' }}</p>
        <router-link
          :to="`/dashboard/courses/${course.id}`"
          class="mt-auto px-4 py-2 rounded-lg bg-blue-600 text-white font-semibold hover:bg-blue-700 transition text-center"
        >
          Continue
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useCourseStore } from '@/stores/courseStore'

const courseStore = useCourseStore()

const { courses, loading, error, fetchCourses } = courseStore
console.log(courses)

onMounted(() => {
  fetchCourses()
})
</script>
