from rest_framework import viewsets
from django.shortcuts import redirect, render
from .models import Course, Module, Lesson
from .serializers import CourseSerializer, ModuleSerializer, LessonSerializer
from .permissions import IsInstructorOrReadOnly
from .forms import LessonFileForm

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsInstructorOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.role == 'instructor':
            return Course.objects.filter(instructor=user)
        return Course.objects.filter(visibility='published')

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

def upload_file(request):
    if request.method == 'POST':
        form = LessonFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = LessonFileForm()
    return render(request, 'upload.html', {'form': form})
