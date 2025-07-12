<script setup lang="ts">
import { ref } from 'vue'

const stats = ref({
  totalStudents: 1247,
  totalCourses: 89,
  totalInstructors: 23,
  totalRevenue: 45678,
})

const recentStudents = ref([
  { id: 1, name: 'John Doe', email: 'john@example.com', status: 'Active', joined: '2024-01-15' },
  { id: 2, name: 'Jane Smith', email: 'jane@example.com', status: 'Active', joined: '2024-01-14' },
  {
    id: 3,
    name: 'Mike Johnson',
    email: 'mike@example.com',
    status: 'Pending',
    joined: '2024-01-13',
  },
  {
    id: 4,
    name: 'Sarah Wilson',
    email: 'sarah@example.com',
    status: 'Active',
    joined: '2024-01-12',
  },
])

const recentCourses = ref([
  {
    id: 1,
    title: 'Advanced JavaScript',
    instructor: 'Dr. Smith',
    students: 45,
    status: 'Published',
  },
  {
    id: 2,
    title: 'Python for Beginners',
    instructor: 'Prof. Johnson',
    students: 78,
    status: 'Draft',
  },
  { id: 3, title: 'React Development', instructor: 'Ms. Davis', students: 32, status: 'Published' },
  {
    id: 4,
    title: 'Data Science Fundamentals',
    instructor: 'Dr. Brown',
    students: 56,
    status: 'Published',
  },
])

const systemAlerts = ref([
  {
    id: 1,
    type: 'warning',
    message: 'Server maintenance scheduled for tonight',
    time: '2 hours ago',
  },
  { id: 2, type: 'info', message: 'New course submission pending review', time: '4 hours ago' },
  { id: 3, type: 'success', message: 'Payment system updated successfully', time: '1 day ago' },
])

const activeTab = ref('overview')

const tabs = [
  { id: 'overview', name: 'Overview', icon: 'chart-bar' },
  { id: 'students', name: 'Students', icon: 'users' },
  { id: 'courses', name: 'Courses', icon: 'book-open' },
  { id: 'instructors', name: 'Instructors', icon: 'chalkboard-teacher' },
  { id: 'analytics', name: 'Analytics', icon: 'chart-line' },
  { id: 'settings', name: 'Settings', icon: 'cog' },
]
</script>

<template>
  <div class="w-full mx-auto">
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-800 mb-2">Admin Panel</h1>
      <p class="text-gray-600">Manage your learning platform and monitor system performance</p>
    </div>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 mb-8">
      <div class="flex overflow-x-auto no-scrollbar">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          @click="activeTab = tab.id"
          :class="[
            'flex items-center gap-2 px-6 py-4 font-semibold border-b-2 transition-colors whitespace-nowrap',
            activeTab === tab.id
              ? 'border-blue-600 text-blue-600 bg-blue-50'
              : 'border-transparent text-gray-600 hover:text-gray-800 hover:bg-gray-50',
          ]"
        >
          <font-awesome-icon :icon="['fas', tab.icon]" class="text-lg" />
          {{ tab.name }}
        </button>
      </div>
    </div>

    <div v-if="activeTab === 'overview'" class="space-y-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">Total Students</p>
              <p class="text-3xl font-bold text-gray-800">
                {{ stats.totalStudents.toLocaleString() }}
              </p>
            </div>
            <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
              <font-awesome-icon :icon="['fas', 'users']" class="text-2xl text-blue-600" />
            </div>
          </div>
          <div class="mt-4 flex items-center text-sm text-green-600">
            <font-awesome-icon :icon="['fas', 'arrow-up']" class="mr-1" />
            +12% from last month
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">Total Courses</p>
              <p class="text-3xl font-bold text-gray-800">{{ stats.totalCourses }}</p>
            </div>
            <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
              <font-awesome-icon :icon="['fas', 'book-open']" class="text-2xl text-green-600" />
            </div>
          </div>
          <div class="mt-4 flex items-center text-sm text-green-600">
            <font-awesome-icon :icon="['fas', 'arrow-up']" class="mr-1" />
            +5 new this week
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">Instructors</p>
              <p class="text-3xl font-bold text-gray-800">{{ stats.totalInstructors }}</p>
            </div>
            <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
              <font-awesome-icon
                :icon="['fas', 'chalkboard-teacher']"
                class="text-2xl text-purple-600"
              />
            </div>
          </div>
          <div class="mt-4 flex items-center text-sm text-green-600">
            <font-awesome-icon :icon="['fas', 'arrow-up']" class="mr-1" />
            +2 new this month
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">Revenue</p>
              <p class="text-3xl font-bold text-gray-800">
                ${{ stats.totalRevenue.toLocaleString() }}
              </p>
            </div>
            <div class="w-12 h-12 bg-yellow-100 rounded-lg flex items-center justify-center">
              <font-awesome-icon :icon="['fas', 'dollar-sign']" class="text-2xl text-yellow-600" />
            </div>
          </div>
          <div class="mt-4 flex items-center text-sm text-green-600">
            <font-awesome-icon :icon="['fas', 'arrow-up']" class="mr-1" />
            +8% from last month
          </div>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div class="flex items-center justify-between mb-6">
            <h3 class="text-xl font-bold text-gray-800">Recent Students</h3>
            <button class="text-blue-600 hover:text-blue-700 font-semibold">View All</button>
          </div>
          <div class="space-y-4">
            <div
              v-for="student in recentStudents"
              :key="student.id"
              class="flex items-center justify-between p-4 bg-gray-50 rounded-lg"
            >
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                  <font-awesome-icon :icon="['fas', 'user']" class="text-blue-600" />
                </div>
                <div>
                  <p class="font-semibold text-gray-800">{{ student.name }}</p>
                  <p class="text-sm text-gray-600">{{ student.email }}</p>
                </div>
              </div>
              <div class="text-right">
                <span
                  :class="[
                    'px-2 py-1 rounded-full text-xs font-semibold',
                    student.status === 'Active'
                      ? 'bg-green-100 text-green-700'
                      : 'bg-yellow-100 text-yellow-700',
                  ]"
                >
                  {{ student.status }}
                </span>
                <p class="text-xs text-gray-500 mt-1">{{ student.joined }}</p>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div class="flex items-center justify-between mb-6">
            <h3 class="text-xl font-bold text-gray-800">Recent Courses</h3>
            <button class="text-blue-600 hover:text-blue-700 font-semibold">View All</button>
          </div>
          <div class="space-y-4">
            <div
              v-for="course in recentCourses"
              :key="course.id"
              class="flex items-center justify-between p-4 bg-gray-50 rounded-lg"
            >
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center">
                  <font-awesome-icon :icon="['fas', 'book']" class="text-green-600" />
                </div>
                <div>
                  <p class="font-semibold text-gray-800">{{ course.title }}</p>
                  <p class="text-sm text-gray-600">{{ course.instructor }}</p>
                </div>
              </div>
              <div class="text-right">
                <span
                  :class="[
                    'px-2 py-1 rounded-full text-xs font-semibold',
                    course.status === 'Published'
                      ? 'bg-green-100 text-green-700'
                      : 'bg-gray-100 text-gray-700',
                  ]"
                >
                  {{ course.status }}
                </span>
                <p class="text-xs text-gray-500 mt-1">{{ course.students }} students</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <h3 class="text-xl font-bold text-gray-800 mb-6">System Alerts</h3>
        <div class="space-y-4">
          <div
            v-for="alert in systemAlerts"
            :key="alert.id"
            class="flex items-center gap-4 p-4 rounded-lg"
            :class="{
              'bg-yellow-50 border border-yellow-200': alert.type === 'warning',
              'bg-blue-50 border border-blue-200': alert.type === 'info',
              'bg-green-50 border border-green-200': alert.type === 'success',
            }"
          >
            <div
              class="w-8 h-8 rounded-full flex items-center justify-center"
              :class="{
                'bg-yellow-100': alert.type === 'warning',
                'bg-blue-100': alert.type === 'info',
                'bg-green-100': alert.type === 'success',
              }"
            >
              <font-awesome-icon
                :icon="[
                  'fas',
                  alert.type === 'warning'
                    ? 'exclamation-triangle'
                    : alert.type === 'info'
                      ? 'info-circle'
                      : 'check-circle',
                ]"
                :class="{
                  'text-yellow-600': alert.type === 'warning',
                  'text-blue-600': alert.type === 'info',
                  'text-green-600': alert.type === 'success',
                }"
              />
            </div>
            <div class="flex-1">
              <p class="font-medium text-gray-800">{{ alert.message }}</p>
              <p class="text-sm text-gray-500">{{ alert.time }}</p>
            </div>
            <button class="text-gray-400 hover:text-gray-600">
              <font-awesome-icon :icon="['fas', 'times']" />
            </button>
          </div>
        </div>
      </div>
    </div>

    <div v-if="activeTab === 'students'" class="space-y-8">
      <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-xl font-bold text-gray-800">Student Management</h3>
          <button
            class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-semibold"
          >
            <font-awesome-icon :icon="['fas', 'plus']" class="mr-2" />
            Add Student
          </button>
        </div>

        <div class="flex flex-col md:flex-row gap-4 mb-6">
          <div class="flex-1">
            <div class="relative">
              <font-awesome-icon
                :icon="['fas', 'search']"
                class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"
              />
              <input
                type="text"
                placeholder="Search students..."
                class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
          </div>
          <select
            class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          >
            <option>All Status</option>
            <option>Active</option>
            <option>Pending</option>
            <option>Suspended</option>
          </select>
          <select
            class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          >
            <option>Sort by</option>
            <option>Name</option>
            <option>Join Date</option>
            <option>Status</option>
          </select>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full">
            <thead class="bg-gray-50">
              <tr>
                <th
                  class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Student
                </th>
                <th
                  class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Email
                </th>
                <th
                  class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Status
                </th>
                <th
                  class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Joined
                </th>
                <th
                  class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Actions
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="student in recentStudents" :key="student.id" class="hover:bg-gray-50">
                <td class="px-4 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div
                      class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center mr-3"
                    >
                      <font-awesome-icon :icon="['fas', 'user']" class="text-blue-600 text-sm" />
                    </div>
                    <div class="text-sm font-medium text-gray-900">{{ student.name }}</div>
                  </div>
                </td>
                <td class="px-4 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ student.email }}
                </td>
                <td class="px-4 py-4 whitespace-nowrap">
                  <span
                    :class="[
                      'px-2 py-1 text-xs font-semibold rounded-full',
                      student.status === 'Active'
                        ? 'bg-green-100 text-green-700'
                        : 'bg-yellow-100 text-yellow-700',
                    ]"
                  >
                    {{ student.status }}
                  </span>
                </td>
                <td class="px-4 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ student.joined }}
                </td>
                <td class="px-4 py-4 whitespace-nowrap text-sm font-medium">
                  <button class="text-blue-600 hover:text-blue-900 mr-3">Edit</button>
                  <button class="text-red-600 hover:text-red-900">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div v-if="activeTab === 'courses'" class="space-y-8">
      <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-xl font-bold text-gray-800">Course Management</h3>
          <button
            class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-semibold"
          >
            <font-awesome-icon :icon="['fas', 'plus']" class="mr-2" />
            Add Course
          </button>
        </div>

        <div class="flex flex-col md:flex-row gap-4 mb-6">
          <div class="flex-1">
            <div class="relative">
              <font-awesome-icon
                :icon="['fas', 'search']"
                class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"
              />
              <input
                type="text"
                placeholder="Search courses..."
                class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
          </div>
          <select
            class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-black"
          >
            <option>All Categories</option>
            <option>Programming</option>
            <option>Design</option>
            <option>Business</option>
          </select>
          <select
            class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-black"
          >
            <option>All Status</option>
            <option>Published</option>
            <option>Draft</option>
            <option>Archived</option>
          </select>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full">
            <thead class="bg-gray-50">
              <tr>
                <th
                  class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Course
                </th>
                <th
                  class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Instructor
                </th>
                <th
                  class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Students
                </th>
                <th
                  class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Status
                </th>
                <th
                  class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Actions
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="course in recentCourses" :key="course.id" class="hover:bg-gray-50">
                <td class="px-4 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div
                      class="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center mr-3"
                    >
                      <font-awesome-icon :icon="['fas', 'book']" class="text-green-600 text-sm" />
                    </div>
                    <div class="text-sm font-medium text-gray-900">{{ course.title }}</div>
                  </div>
                </td>
                <td class="px-4 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ course.instructor }}
                </td>
                <td class="px-4 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ course.students }}
                </td>
                <td class="px-4 py-4 whitespace-nowrap">
                  <span
                    :class="[
                      'px-2 py-1 text-xs font-semibold rounded-full',
                      course.status === 'Published'
                        ? 'bg-green-100 text-green-700'
                        : 'bg-gray-100 text-gray-700',
                    ]"
                  >
                    {{ course.status }}
                  </span>
                </td>
                <td class="px-4 py-4 whitespace-nowrap text-sm font-medium">
                  <button class="text-blue-600 hover:text-blue-900 mr-3">Edit</button>
                  <button class="text-green-600 hover:text-green-900 mr-3">View</button>
                  <button class="text-red-600 hover:text-red-900">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div v-if="activeTab === 'instructors'" class="space-y-8">
      <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-xl font-bold text-gray-800">Instructor Management</h3>
          <button
            class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-semibold"
          >
            <font-awesome-icon :icon="['fas', 'plus']" class="mr-2" />
            Add Instructor
          </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div class="bg-blue-50 rounded-lg p-4">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-blue-600">Total Instructors</p>
                <p class="text-2xl font-bold text-blue-800">23</p>
              </div>
              <font-awesome-icon
                :icon="['fas', 'chalkboard-teacher']"
                class="text-2xl text-blue-600"
              />
            </div>
          </div>
          <div class="bg-green-50 rounded-lg p-4">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-green-600">Active Courses</p>
                <p class="text-2xl font-bold text-green-800">67</p>
              </div>
              <font-awesome-icon :icon="['fas', 'book-open']" class="text-2xl text-green-600" />
            </div>
          </div>
          <div class="bg-purple-50 rounded-lg p-4">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-purple-600">Avg. Rating</p>
                <p class="text-2xl font-bold text-purple-800">4.8</p>
              </div>
              <font-awesome-icon :icon="['fas', 'star']" class="text-2xl text-purple-600" />
            </div>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="i in 6" :key="i" class="bg-gray-50 rounded-lg p-6 border border-gray-200">
            <div class="flex items-center gap-4 mb-4">
              <img
                :src="`https://randomuser.me/api/portraits/men/${i + 20}.jpg`"
                class="w-12 h-12 rounded-full"
                alt="Instructor"
              />
              <div>
                <h4 class="font-semibold text-gray-800">Dr. Instructor {{ i }}</h4>
                <p class="text-sm text-gray-600">Computer Science</p>
              </div>
            </div>
            <div class="space-y-2 mb-4">
              <div class="flex justify-between text-sm">
                <span class="text-gray-600">Courses:</span>
                <span class="font-semibold">{{ Math.floor(Math.random() * 10) + 1 }}</span>
              </div>
              <div class="flex justify-between text-sm">
                <span class="text-gray-600">Students:</span>
                <span class="font-semibold">{{ Math.floor(Math.random() * 500) + 50 }}</span>
              </div>
              <div class="flex justify-between text-sm">
                <span class="text-gray-600">Rating:</span>
                <span class="font-semibold text-yellow-600"
                  >4.{{ Math.floor(Math.random() * 9) + 1 }}</span
                >
              </div>
            </div>
            <div class="flex gap-2">
              <button
                class="flex-1 px-3 py-2 bg-blue-600 text-white text-sm rounded-lg hover:bg-blue-700"
              >
                View Profile
              </button>
              <button
                class="px-3 py-2 bg-gray-200 text-gray-700 text-sm rounded-lg hover:bg-gray-300"
              >
                <font-awesome-icon :icon="['fas', 'edit']" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="activeTab === 'analytics'" class="space-y-8">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h3 class="text-xl font-bold text-gray-800 mb-6">Revenue Overview</h3>
          <div class="h-64 bg-gray-100 rounded-lg flex items-center justify-center">
            <p class="text-gray-500">Chart placeholder - Revenue data visualization</p>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h3 class="text-xl font-bold text-gray-800 mb-6">Student Growth</h3>
          <div class="h-64 bg-gray-100 rounded-lg flex items-center justify-center">
            <p class="text-gray-500">Chart placeholder - Student growth visualization</p>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h3 class="text-xl font-bold text-gray-800 mb-6">Top Performing Courses</h3>
          <div class="space-y-4">
            <div
              v-for="(course, index) in recentCourses.slice(0, 5)"
              :key="course.id"
              class="flex items-center justify-between p-4 bg-gray-50 rounded-lg"
            >
              <div class="flex items-center gap-3">
                <div
                  class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center text-sm font-bold text-blue-600"
                >
                  {{ index + 1 }}
                </div>
                <div>
                  <p class="font-semibold text-gray-800">{{ course.title }}</p>
                  <p class="text-sm text-gray-600">{{ course.students }} students</p>
                </div>
              </div>
              <div class="text-right">
                <p class="font-semibold text-green-600">
                  ${{ Math.floor(Math.random() * 5000) + 1000 }}
                </p>
                <p class="text-sm text-gray-500">Revenue</p>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h3 class="text-xl font-bold text-gray-800 mb-6">System Metrics</h3>
          <div class="space-y-4">
            <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center">
                  <font-awesome-icon :icon="['fas', 'server']" class="text-green-600" />
                </div>
                <div>
                  <p class="font-semibold text-gray-800">Server Uptime</p>
                  <p class="text-sm text-gray-600">System performance</p>
                </div>
              </div>
              <div class="text-right">
                <p class="font-semibold text-green-600">99.9%</p>
                <p class="text-sm text-gray-500">Last 30 days</p>
              </div>
            </div>
            <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center">
                  <font-awesome-icon :icon="['fas', 'database']" class="text-blue-600" />
                </div>
                <div>
                  <p class="font-semibold text-gray-800">Database</p>
                  <p class="text-sm text-gray-600">Storage usage</p>
                </div>
              </div>
              <div class="text-right">
                <p class="font-semibold text-blue-600">67%</p>
                <p class="text-sm text-gray-500">Used</p>
              </div>
            </div>
            <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 bg-yellow-100 rounded-full flex items-center justify-center">
                  <font-awesome-icon :icon="['fas', 'users']" class="text-yellow-600" />
                </div>
                <div>
                  <p class="font-semibold text-gray-800">Active Users</p>
                  <p class="text-sm text-gray-600">Current online</p>
                </div>
              </div>
              <div class="text-right">
                <p class="font-semibold text-yellow-600">1,247</p>
                <p class="text-sm text-gray-500">Users</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="activeTab === 'settings'" class="space-y-8">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h3 class="text-xl font-bold text-gray-800 mb-6">General Settings</h3>
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Platform Name</label>
              <input
                type="text"
                value="Smart Learning Platform"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Contact Email</label>
              <input
                type="email"
                value="admin@smartlearning.com"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Timezone</label>
              <select
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option>UTC (Coordinated Universal Time)</option>
                <option>EST (Eastern Standard Time)</option>
                <option>PST (Pacific Standard Time)</option>
              </select>
            </div>
            <div class="flex items-center justify-between">
              <div>
                <label class="text-sm font-medium text-gray-700">Maintenance Mode</label>
                <p class="text-sm text-gray-500">Temporarily disable the platform</p>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" class="sr-only peer" />
                <div
                  class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"
                ></div>
              </label>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h3 class="text-xl font-bold text-gray-800 mb-6">Security Settings</h3>
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <div>
                <label class="text-sm font-medium text-gray-700">Two-Factor Authentication</label>
                <p class="text-sm text-gray-500">Require 2FA for all users</p>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" checked class="sr-only peer" />
                <div
                  class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"
                ></div>
              </label>
            </div>
            <div class="flex items-center justify-between">
              <div>
                <label class="text-sm font-medium text-gray-700">Session Timeout</label>
                <p class="text-sm text-gray-500">Auto-logout after inactivity</p>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" checked class="sr-only peer" />
                <div
                  class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"
                ></div>
              </label>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2"
                >Session Timeout (minutes)</label
              >
              <input
                type="number"
                value="30"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
            <div class="flex items-center justify-between">
              <div>
                <label class="text-sm font-medium text-gray-700">Email Verification</label>
                <p class="text-sm text-gray-500">Require email verification</p>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" checked class="sr-only peer" />
                <div
                  class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"
                ></div>
              </label>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h3 class="text-xl font-bold text-gray-800 mb-6">Notification Settings</h3>
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <div>
                <label class="text-sm font-medium text-gray-700">Email Notifications</label>
                <p class="text-sm text-gray-500">Send email alerts</p>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" checked class="sr-only peer" />
                <div
                  class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"
                ></div>
              </label>
            </div>
            <div class="flex items-center justify-between">
              <div>
                <label class="text-sm font-medium text-gray-700">System Alerts</label>
                <p class="text-sm text-gray-500">Critical system notifications</p>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" checked class="sr-only peer" />
                <div
                  class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"
                ></div>
              </label>
            </div>
            <div class="flex items-center justify-between">
              <div>
                <label class="text-sm font-medium text-gray-700">User Activity</label>
                <p class="text-sm text-gray-500">Track user actions</p>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" class="sr-only peer" />
                <div
                  class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"
                ></div>
              </label>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h3 class="text-xl font-bold text-gray-800 mb-6">Backup & Maintenance</h3>
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <div>
                <label class="text-sm font-medium text-gray-700">Auto Backup</label>
                <p class="text-sm text-gray-500">Daily database backup</p>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" checked class="sr-only peer text-black" />
                <div
                  class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"
                ></div>
              </label>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2"
                >Backup Retention (days)</label
              >
              <input
                type="number"
                value="30"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
            <button
              class="w-full px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 font-semibold"
            >
              <font-awesome-icon :icon="['fas', 'download']" class="mr-2" />
              Create Manual Backup
            </button>
            <button
              class="w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-semibold"
            >
              <font-awesome-icon :icon="['fas', 'sync']" class="mr-2" />
              Check for Updates
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
