import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: () => import('../views/landing/LandingView.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/auth/LoginView.vue'),
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/auth/RegisterView.vue'),
    },
    {
      path: '/forgot-password',
      children: [
        {
          path: 'request',
          name: 'reset-password-request',
          component: () => import('../views/auth/ResetPasswordRequest.vue'),
        },
        {
          path: 'confirm',
          name: 'reset-password-confirm',
          component: () => import('../views/auth/ResetPasswordConfirm.vue'),
        },
      ],
    },
    {
      path: '/dashboard',
      component: () => import('../views/DashboardView.vue'),
      children: [
        { path: '', redirect: '/dashboard/overview' },
        {
          path: 'overview',
          name: 'dashboard-overview',
          component: () => import('../views/HomeView.vue'),
        },
        {
          path: 'courses',
          name: 'dashboard-courses',
          component: () => import('../views/CoursesView.vue'),
        },
        {
          path: 'courses/:id',
          name: 'dashboard-course-detail',
          component: () => import('../views/CourseDetailView.vue'),
        },
        {
          path: 'certificates',
          name: 'dashboard-certificates',
          component: () => import('../views/CertificatesView.vue'),
        },
        {
          path: 'profile',
          name: 'dashboard-profile',
          component: () => import('../views/ProfileView.vue'),
        },
        {
          path: 'reviews',
          name: 'dashboard-reviews',
          component: () => import('../views/ReviewsView.vue'),
        },
        {
          path: 'payment',
          name: 'dashboard-payment',
          component: () => import('../views/PaymentView.vue'),
        },
        {
          path: 'instructor',
          name: 'dashboard-instructor',
          component: () => import('../views/InstructorDashboardView.vue'),
        },
        {
          path: 'course-edit',
          name: 'dashboard-course-edit',
          component: () => import('../views/CourseEditView.vue'),
        },
        {
          path: 'schedule',
          name: 'dashboard-schedule',
          component: () => import('../views/ScheduleView.vue'),
        },
        {
          path: 'messages',
          name: 'dashboard-messages',
          component: () => import('../views/MessagesView.vue'),
        },
        {
          path: 'admin',
          name: 'dashboard-admin',
          component: () => import('../views/AdminView.vue'),
        },
        {
          path: 'assignments',
          name: 'dashboard-assignments',
          component: () => import('../views/AssignmentsView.vue'),
        },
        {
          path: 'subscription',
          name: 'dashboard-subscription',
          component: () => import('../views/SubscriptionView.vue'),
        },
        {
          path: 'wishlist',
          name: 'dashboard-wishlist',
          component: () => import('../views/WishlistView.vue'),
        },
        {
          path: 'community',
          name: 'dashboard-community',
          component: () => import('../views/CommunityView.vue'),
        },
        {
          path: 'achievements',
          name: 'dashboard-achievements',
          component: () => import('../views/AchievementsView.vue'),
        },
        {
          path: 'analytics',
          name: 'dashboard-analytics',
          component: () => import('../views/AnalyticsView.vue'),
        },
        {
          path: 'students',
          name: 'dashboard-students',
          component: () => import('../views/StudentsView.vue'),
        },
      ],
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('../views/NotFoundView.vue'),
    },
  ],
})

export default router
