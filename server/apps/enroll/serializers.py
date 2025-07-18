from rest_framework import serializers
from .models import Enrollment, LessonProgress

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'enrolled_at']


class LessonProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonProgress
        fields = ['id', 'enrollment', 'lesson', 'completed', 'last_accessed']
