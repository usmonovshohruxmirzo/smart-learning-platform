<script setup lang="ts">
import { ref } from 'vue'
const showMore = ref<boolean>(false)
function toggleMore(): void {
  showMore.value = !showMore.value
}
</script>
<template>
  <div class="min-h-screen bg-gray-100 flex flex-col">
    <header
      class="w-full flex items-center justify-between px-6 h-16 z-10 bg-white border-b border-gray-200"
    >
      <div class="text-xl font-bold text-blue-600 tracking-tight">Smart Learning</div>
      <div class="flex items-center gap-4">
        <button class="rounded-full bg-blue-50 p-2 hover:bg-blue-100">
          <svg
            class="w-6 h-6 text-blue-600"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
            />
          </svg>
        </button>
        <img
          src="https://randomuser.me/api/portraits/men/32.jpg"
          class="w-10 h-10 rounded-full border-2 border-blue-500"
          alt="User"
        />
      </div>
    </header>

    <div class="flex flex-1 h-[calc(100vh-4rem)]">
      <aside
        class="hidden md:flex flex-col w-72 bg-white border-r border-gray-200 py-8 px-4 gap-2 fixed top-16 left-0 h-[calc(100vh-4rem)] z-20 overflow-y-auto no-scrollbar"
      >
        <nav class="flex flex-col gap-2">
          <div class="mb-2 text-gray-700">
            <div class="text-xs font-bold text-gray-400 uppercase mb-1">Main</div>
            <router-link
              to="/dashboard/overview"
              class="flex items-center gap-2 px-3 py-2 rounded-lg font-semibold"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'book-open']" class="text-lg" /> Overview
            </router-link>
            <router-link
              to="/dashboard/courses"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'book-open']" class="text-lg" /> My Courses
            </router-link>
            <router-link
              to="/dashboard/assignments"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'tasks']" class="text-lg" /> Assignments
            </router-link>
            <router-link
              to="/dashboard/schedule"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'calendar']" class="text-lg" /> Schedule
            </router-link>
          </div>

          <div class="mb-2 text-gray-700">
            <div class="text-xs font-bold text-gray-400 uppercase mb-1">Learning</div>
            <router-link
              to="/dashboard/wishlist"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'heart']" class="text-lg" /> Wishlist
            </router-link>
            <router-link
              to="/dashboard/community"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'comments']" class="text-lg" /> Community
            </router-link>
            <router-link
              to="/dashboard/achievements"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'trophy']" class="text-lg" /> Achievements
            </router-link>
            <router-link
              to="/dashboard/analytics"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'chart-bar']" class="text-lg" /> Analytics
            </router-link>
          </div>

          <div class="mb-2 text-gray-700">
            <div class="text-xs font-bold text-gray-400 uppercase mb-1">Account</div>
            <router-link
              to="/dashboard/profile"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'users']" class="text-lg" /> Profile
            </router-link>
            <router-link
              to="/dashboard/certificates"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'certificate']" class="text-lg" /> Certificates
            </router-link>
            <router-link
              to="/dashboard/reviews"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'star']" class="text-lg" /> Reviews
            </router-link>
            <router-link
              to="/dashboard/subscription"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'credit-card']" class="text-lg" /> Subscription
            </router-link>
            <router-link
              to="/dashboard/payment"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'dollar-sign']" class="text-lg" /> Payment
            </router-link>
          </div>

          <div class="text-gray-700">
            <div class="text-xs font-bold text-gray-400 uppercase mb-1">Admin</div>
            <router-link
              to="/dashboard/students"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'graduation-cap']" class="text-lg" /> Students
            </router-link>
            <router-link
              to="/dashboard/instructor"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'users']" class="text-lg" /> Instructor
            </router-link>
            <router-link
              to="/dashboard/admin"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'user-shield']" class="text-lg" /> Admin Panel
            </router-link>
            <router-link
              to="/dashboard/course-edit"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'book-open']" class="text-lg" /> Course Edit
            </router-link>
            <router-link
              to="/dashboard/messages"
              class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-100"
              active-class="bg-blue-100 text-blue-700"
            >
              <font-awesome-icon :icon="['fas', 'envelope']" class="text-lg" /> Messages
            </router-link>
          </div>
        </nav>
      </aside>
      <main
        class="flex-1 p-6 flex flex-col gap-8 ml-0 md:ml-72 overflow-y-auto h-[calc(100vh-4rem)] no-scrollbar pb-[120px]"
      >
        <router-view />
      </main>
    </div>

    <nav
      class="fixed bottom-0 left-0 right-0 z-30 bg-white border-t border-gray-200 flex items-center h-20 md:hidden shadow-xl text-gray-700"
      role="navigation"
      aria-label="Main mobile navigation"
    >
      <router-link
        to="/dashboard/overview"
        class="flex flex-col items-center justify-center flex-1 h-full focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500"
        active-class="text-blue-700"
        aria-label="Overview"
      >
        <font-awesome-icon :icon="['fas', 'book-open']" class="text-2xl mb-1" aria-hidden="true" />
        <span class="text-xs font-semibold">Overview</span>
      </router-link>
      <router-link
        to="/dashboard/courses"
        class="flex flex-col items-center justify-center flex-1 h-full focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500"
        active-class="text-blue-700"
        aria-label="Courses"
      >
        <font-awesome-icon :icon="['fas', 'book-open']" class="text-2xl mb-1" aria-hidden="true" />
        <span class="text-xs font-semibold">Courses</span>
      </router-link>
      <router-link
        to="/dashboard/assignments"
        class="flex flex-col items-center justify-center flex-1 h-full focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500"
        active-class="text-blue-700"
        aria-label="Assignments"
      >
        <font-awesome-icon :icon="['fas', 'tasks']" class="text-2xl mb-1" aria-hidden="true" />
        <span class="text-xs font-semibold">Tasks</span>
      </router-link>
      <router-link
        to="/dashboard/profile"
        class="flex flex-col items-center justify-center flex-1 h-full focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500"
        active-class="text-blue-700"
        aria-label="Profile"
      >
        <font-awesome-icon :icon="['fas', 'users']" class="text-2xl mb-1" aria-hidden="true" />
        <span class="text-xs font-semibold">Profile</span>
      </router-link>

      <button
        @click="toggleMore"
        class="flex flex-col items-center justify-center flex-1 h-full focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 relative"
        aria-label="More"
      >
        <font-awesome-icon :icon="['fas', 'list-ul']" class="text-2xl mb-1" />
        <span class="text-xs font-semibold">More</span>
      </button>

      <div
        v-if="showMore"
        class="fixed left-0 right-0 bottom-20 z-50 flex justify-center md:hidden pointer-events-none p-5"
      >
        <div
          class="bg-white w-screen p-5 flex flex-col gap-1 max-h-60 overflow-y-auto border pointer-events-auto no-scrollbar rounded-[5]"
        >
          <router-link
            to="/dashboard/schedule"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
            active-class="bg-blue-100 text-blue-700"
          >
            <font-awesome-icon :icon="['fas', 'calendar']" class="text-lg" aria-hidden="true" />
            Schedule
          </router-link>
          <router-link
            to="/dashboard/wishlist"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
          >
            <font-awesome-icon :icon="['fas', 'heart']" class="text-lg" aria-hidden="true" />
            Wishlist
          </router-link>
          <router-link
            to="/dashboard/community"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
          >
            <font-awesome-icon :icon="['fas', 'comments']" class="text-lg" aria-hidden="true" />
            Community
          </router-link>
          <router-link
            to="/dashboard/achievements"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
          >
            <font-awesome-icon :icon="['fas', 'trophy']" class="text-lg" aria-hidden="true" />
            Achievements
          </router-link>
          <router-link
            to="/dashboard/analytics"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
          >
            <font-awesome-icon :icon="['fas', 'chart-bar']" class="text-lg" aria-hidden="true" />
            Analytics
          </router-link>
          <router-link
            to="/dashboard/certificates"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
          >
            <font-awesome-icon :icon="['fas', 'certificate']" class="text-lg" aria-hidden="true" />
            Certificates
          </router-link>
          <router-link
            to="/dashboard/reviews"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
          >
            <font-awesome-icon :icon="['fas', 'star']" class="text-lg" aria-hidden="true" /> Reviews
          </router-link>
          <router-link
            to="/dashboard/subscription"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
          >
            <font-awesome-icon :icon="['fas', 'credit-card']" class="text-lg" aria-hidden="true" />
            Subscription
          </router-link>
          <router-link
            to="/dashboard/payment"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
          >
            <font-awesome-icon :icon="['fas', 'dollar-sign']" class="text-lg" aria-hidden="true" />
            Payment
          </router-link>
          <router-link
            to="/dashboard/instructor"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
          >
            <font-awesome-icon :icon="['fas', 'users']" class="text-lg" aria-hidden="true" />
            Instructor
          </router-link>
          <router-link
            to="/dashboard/admin"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
          >
            <font-awesome-icon :icon="['fas', 'user-shield']" class="text-lg" aria-hidden="true" />
            Admin Panel
          </router-link>
          <router-link
            to="/dashboard/course-edit"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
          >
            <font-awesome-icon :icon="['fas', 'book-open']" class="text-lg" aria-hidden="true" />
            Course Edit
          </router-link>
          <router-link
            to="/dashboard/students"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
          >
            <font-awesome-icon
              :icon="['fas', 'graduation-cap']"
              class="text-lg"
              aria-hidden="true"
            />
            Students
          </router-link>
          <router-link
            to="/dashboard/messages"
            class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-100"
            @click="toggleMore"
          >
            <font-awesome-icon :icon="['fas', 'envelope']" class="text-lg" aria-hidden="true" />
            Messages
          </router-link>
        </div>
      </div>
    </nav>
  </div>
</template>
