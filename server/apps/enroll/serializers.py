from rest_framework import serializers
from .models import Enrollment
from .lesson_progress_serializer import LessonProgressSerializer

class EnrollmentSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(source='course.id')
    course_title = serializers.CharField(source='course.title')
    lesson_progress = LessonProgressSerializer(source='lessonprogress_set', many=True, read_only=True)

    class Meta:
        model = Enrollment
        fields = ['course_id', 'course_title', 'enrolled_at', 'lesson_progress']
