import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue'),
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/Register.vue'),
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/About.vue'),
    },
    {
      path: '/dashboard',
      component: () => import('../views/Dashboard.vue'),
      children: [
        {
          path: '',
          redirect: '/dashboard/overview',
        },
        {
          path: 'overview',
          name: 'dashboard-overview',
          component: () => import('../views/Home.vue'),
        },
        {
          path: 'courses',
          name: 'dashboard-courses',
          component: () => import('../views/Courses.vue'),
        },
        {
          path: 'certificates',
          name: 'dashboard-certificates',
          component: () => import('../views/Certificates.vue'),
        },
        {
          path: 'profile',
          name: 'dashboard-profile',
          component: () => import('../views/Profile.vue'),
        },
        {
          path: 'reviews',
          name: 'dashboard-reviews',
          component: () => import('../views/Reviews.vue'),
        },
        {
          path: 'payment',
          name: 'dashboard-payment',
          component: () => import('../views/Payment.vue'),
        },
        {
          path: 'instructor',
          name: 'dashboard-instructor',
          component: () => import('../views/InstructorDashboard.vue'),
        },
        {
          path: 'course-edit',
          name: 'dashboard-course-edit',
          component: () => import('../views/CourseEdit.vue'),
        },
      ],
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('../views/NotFound.vue'),
    },
  ],
})

export default router
