from django.urls import path
from .views import EnrollView, MarkLessonCompleteView, CourseProgressView
from .views import get_user_enrollments

urlpatterns = [
    path('enroll/', EnrollView.as_view(), name='enroll'),
    path('lesson-complete/', MarkLessonCompleteView.as_view(), name='lesson-complete'),
    path('progress/<int:course_id>/', CourseProgressView.as_view(), name='course-progress'),
    path('my-courses/', get_user_enrollments, name='my-courses'),
]
