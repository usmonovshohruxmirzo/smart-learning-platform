from django.db import models
from django.conf import settings

class Course(models.Model):

    VISIBILITY_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


class Lesson(models.Model):
    module = models.ForeignKey(Module, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    video_url = models.URLField(blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    is_preview = models.BooleanField(default=False)


class LessonFile(models.Model):
    FILE_TYPES = [
        ('video', 'Video'),
        ('pdf', 'PDF'),
        ('image', 'Image'),
        ('file', 'File'),
    ]
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='files')
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)
    file = models.FileField(upload_to='lesson_files/')

    def __str__(self):
        return f"{self.file_type} - {self.file.name}"
    
class LessonAssignment(models.Model):
    lesson = models.OneToOneField(
        Lesson, 
        on_delete=models.CASCADE, 
        related_name='assignment'
    )
    question = models.TextField()
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return f"Assignment for {self.lesson.title}"


class LessonQuiz(models.Model):
    lesson = models.OneToOneField(
        Lesson, 
        on_delete=models.CASCADE, 
        related_name='quiz'
    )
    question = models.CharField(max_length=255)

    def __str__(self):
        return f"Quiz for {self.lesson.title}"


class QuizOption(models.Model):
    quiz = models.ForeignKey(
        LessonQuiz, 
        on_delete=models.CASCADE, 
        related_name='options'
    )
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Wrong'})"