from rest_framework import generics, permissions, status
from rest_framework.response import Response
from courses.models import Course
from .models import Enrollment, LessonProgress
from .serializers import EnrollmentSerializer, LessonProgressSerializer
from django.shortcuts import get_object_or_404

class EnrollView():
    pass

class MarkLessonCompleteView():
    pass

class CourseProgressView():
    pass