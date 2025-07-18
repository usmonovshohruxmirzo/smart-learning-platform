from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Enrollment, LessonProgress
from apps.courses.models import Course, Lesson
from .serializers import EnrollmentSerializer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.generics import RetrieveAPIView


class EnrollView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentSerializer

    def post(self, request, *args, **kwargs):
        course_id = request.data.get('course_id')
        course = Course.objects.get(id=course_id)
        enrollment, created = Enrollment.objects.get_or_create(
            student=request.user, course=course
        )
        return Response({'enrolled': True}, status=201)


class MarkLessonCompleteView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        lesson_id = request.data.get('lesson_id')
        lesson = Lesson.objects.get(id=lesson_id)
        enrollment = Enrollment.objects.get(student=request.user, course=lesson.module.course)
        progress, created = LessonProgress.objects.get_or_create(enrollment=enrollment, lesson=lesson)
        progress.completed = True
        progress.save()
        return Response({'lesson_completed': True})


class CourseProgressView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)
        enrollment = Enrollment.objects.get(student=request.user, course=course)
        total_lessons = Lesson.objects.filter(module__course=course).count()
        completed = LessonProgress.objects.filter(enrollment=enrollment, completed=True).count()
        progress_percent = (completed / total_lessons) * 100 if total_lessons else 0
        return Response({
            'total_lessons': total_lessons,
            'completed_lessons': completed,
            'progress': round(progress_percent, 2)
        })

class EnrollmentDetailView(RetrieveAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    
@login_required
def get_user_enrollments(request):
    user = request.user
    enrollments = user.enrollments.select_related("course")

    data = []
    for enrollment in enrollments:
        lessons = Lesson.objects.filter(module__course=enrollment.course)
        total_lessons = lessons.count()

        completed_lessons_qs = LessonProgress.objects.filter(
            enrollment=enrollment, completed=True
        )

        completed_lessons = completed_lessons_qs.count()
        completed = completed_lessons == total_lessons and total_lessons > 0

        last_completed_progress = completed_lessons_qs.order_by("-completed_at").first()
        completed_at = (
            last_completed_progress.completed_at.isoformat()
            if completed and last_completed_progress and last_completed_progress.completed_at
            else None
        )

        data.append({
            "course_id": enrollment.course.id,
            "course_title": enrollment.course.title,
            "enrolled_at": enrollment.enrolled_at.isoformat(),
            "completed": completed,
            "completed_at": completed_at
        })
    
    return JsonResponse({"enrolled_courses": data})