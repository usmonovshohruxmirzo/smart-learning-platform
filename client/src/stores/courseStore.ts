import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type {
  Course,
  CourseCreateRequest,
  CourseUpdateRequest,
} from '@/services/courses/types/courseService.type'
import { createCourseService } from '@/services/courses/courseService'
import api from '@/api/api'

const courseService = createCourseService(api)

export const useCourseStore = defineStore(
  'course',
  () => {
    const courses = ref<Course[]>([])
    const loading = ref(false)
    const error = ref<string | null>(null)
    const selectedCourse = ref<Course | null>(null)

    const courseCount = computed(() => courses.value.length)

    async function fetchCourses(params?: Record<string, string | number>) {
      loading.value = true
      error.value = null
      try {
        courses.value = await courseService.getCourses(params)
      } catch (err: any) {
        error.value = err.message || 'Failed to fetch courses'
      } finally {
        loading.value = false
      }
    }

    async function fetchCourse(id: string) {
      loading.value = true
      error.value = null
      try {
        selectedCourse.value = await courseService.getCourse(id)
      } catch (err: any) {
        error.value = err.message || `Failed to fetch course ${id}`
      } finally {
        loading.value = false
      }
    }

    async function createCourse(data: CourseCreateRequest) {
      loading.value = true
      error.value = null
      try {
        const newCourse = await courseService.createCourse(data)
        courses.value.push(newCourse)
      } catch (err: any) {
        error.value = err.message || 'Failed to create course'
      } finally {
        loading.value = false
      }
    }

    async function updateCourse(id: string, data: CourseUpdateRequest) {
      loading.value = true
      error.value = null
      try {
        const updated = await courseService.updateCourse(id, data)
        const index = courses.value.findIndex((c) => c.id === id)
        if (index !== -1) {
          courses.value[index] = updated
        }
        if (selectedCourse.value?.id === id) {
          selectedCourse.value = updated
        }
      } catch (err: any) {
        error.value = err.message || `Failed to update course ${id}`
      } finally {
        loading.value = false
      }
    }

    async function deleteCourse(id: string) {
      loading.value = true
      error.value = null
      try {
        await courseService.deleteCourse(id)
        courses.value = courses.value.filter((c) => c.id !== id)
        if (selectedCourse.value?.id === id) {
          selectedCourse.value = null
        }
      } catch (err: any) {
        error.value = err.message || `Failed to delete course ${id}`
      } finally {
        loading.value = false
      }
    }

    return {
      courses,
      loading,
      error,
      selectedCourse,
      courseCount,
      fetchCourses,
      fetchCourse,
      createCourse,
      updateCourse,
      deleteCourse,
    }
  },
  {
    persist: true,
  },
)
