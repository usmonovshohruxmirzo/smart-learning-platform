<template>
  <div class="min-h-screen bg-gray-100 flex flex-col">
    <!-- App Bar -->
    <header class="w-full bg-white shadow-md flex items-center justify-between px-6 h-16">
      <div class="text-xl font-bold text-blue-600 tracking-tight">Smart Learning</div>
      <div class="flex items-center gap-4">
        <button class="rounded-full bg-blue-50 p-2 hover:bg-blue-100">
          <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/></svg>
        </button>
        <img src="https://randomuser.me/api/portraits/men/32.jpg" class="w-10 h-10 rounded-full border-2 border-blue-500" alt="User" />
      </div>
    </header>
    <div class="flex flex-1">
      <!-- Sidebar (desktop only) -->
      <aside class="hidden md:flex flex-col w-56 bg-white border-r border-gray-200 py-8 px-4 gap-2">
        <nav class="flex flex-col gap-2">
          <router-link to="/dashboard/overview" class="flex items-center gap-2 px-3 py-2 rounded-lg text-blue-600 bg-blue-50 font-semibold" active-class="bg-blue-100 text-blue-700">
            <font-awesome-icon :icon="['fas', 'book-open']" class="text-lg" /> Overview
          </router-link>
          <router-link to="/dashboard/courses" class="flex items-center gap-2 px-3 py-2 rounded-lg text-gray-700 hover:bg-gray-100" active-class="bg-blue-100 text-blue-700">
            <font-awesome-icon :icon="['fas', 'book-open']" class="text-lg" /> My Courses
          </router-link>
          <router-link to="/dashboard/certificates" class="flex items-center gap-2 px-3 py-2 rounded-lg text-gray-700 hover:bg-gray-100" active-class="bg-blue-100 text-blue-700">
            <font-awesome-icon :icon="['fas', 'certificate']" class="text-lg" /> Certificates
          </router-link>
          <router-link to="/dashboard/profile" class="flex items-center gap-2 px-3 py-2 rounded-lg text-gray-700 hover:bg-gray-100" active-class="bg-blue-100 text-blue-700">
            <font-awesome-icon :icon="['fas', 'users']" class="text-lg" /> Profile
          </router-link>
          <router-link to="/dashboard/reviews" class="flex items-center gap-2 px-3 py-2 rounded-lg text-gray-700 hover:bg-gray-100" active-class="bg-blue-100 text-blue-700">
            <font-awesome-icon :icon="['fas', 'star']" class="text-lg" /> Reviews
          </router-link>
          <router-link to="/dashboard/payment" class="flex items-center gap-2 px-3 py-2 rounded-lg text-gray-700 hover:bg-gray-100" active-class="bg-blue-100 text-blue-700">
            <font-awesome-icon :icon="['fas', 'dollar-sign']" class="text-lg" /> Payment
          </router-link>
          <router-link to="/dashboard/instructor" class="flex items-center gap-2 px-3 py-2 rounded-lg text-gray-700 hover:bg-gray-100" active-class="bg-blue-100 text-blue-700">
            <font-awesome-icon :icon="['fas', 'users']" class="text-lg" /> Instructor
          </router-link>
          <router-link to="/dashboard/course-edit" class="flex items-center gap-2 px-3 py-2 rounded-lg text-gray-700 hover:bg-gray-100" active-class="bg-blue-100 text-blue-700">
            <font-awesome-icon :icon="['fas', 'book-open']" class="text-lg" /> Course Edit
          </router-link>
        </nav>
      </aside>
      <!-- Main Content -->
      <main class="flex-1 p-6 flex flex-col gap-8">
        <router-view />
      </main>
    </div>
  </div>
</template> 