from rest_framework import serializers
from .models import Course, Module, Lesson, LessonQuiz, QuizOption
from apps.enroll.models import Enrollment

class QuizOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizOption
        fields = ['id', 'text', 'is_correct']

class LessonQuizSerializer(serializers.ModelSerializer):
    options = QuizOptionSerializer(many=True, read_only=True)

    class Meta:
        model = LessonQuiz
        fields = ['id', 'question', 'options']

class LessonSerializer(serializers.ModelSerializer):
    quiz = LessonQuizSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = [
            'id',
            'title',
            'content',
            'video',
            'video_url',
            'pdf',
            'image',
            'file',
            'is_preview',
            'module',
            'quiz',
        ]

class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['id', 'title', 'course', 'lessons']

class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    students_enrolled = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_students_enrolled(self, obj):
        return obj.enrollments.count()