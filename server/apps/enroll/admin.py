from django.contrib import admin
from .models import Enrollment, LessonProgress

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    search_fields = ('student__email', 'course__title')


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'lesson', 'completed', 'completed_at')
    list_filter = ('completed',)
