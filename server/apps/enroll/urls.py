from django.urls import path
from .views import EnrollView, MarkLessonCompleteView, CourseProgressView
from .views import get_user_enrollments, CourseCompleteView

urlpatterns = [
    path('enroll/', EnrollView.as_view(), name='enroll'),
    path('course-complete/<int:course_id>/', CourseCompleteView.as_view(), name='course-complete'),
    path('lesson-complete/', MarkLessonCompleteView.as_view(), name='lesson-complete'),
    path('progress/<int:course_id>/', CourseProgressView.as_view(), name='course-progress'),
    path('my-courses/', get_user_enrollments, name='my-courses'),
]
