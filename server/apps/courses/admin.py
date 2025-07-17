from django.contrib import admin
from .models import Course, Module, Lesson, LessonFile, LessonQuiz, QuizOption

class LessonFileInline(admin.TabularInline):
    model = LessonFile
    extra = 1

class QuizOptionInline(admin.TabularInline):
    model = QuizOption
    extra = 2

class LessonQuizInline(admin.StackedInline):
    model = LessonQuiz
    extra = 1
    show_change_link = True

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "instructor", "visibility", "created_at")
    search_fields = ("title", "description", "instructor__email")
    list_filter = ("visibility", "created_at")
    inlines = [ModuleInline := type('ModuleInline', (admin.StackedInline,), {
        'model': Module,
        'extra': 1,
    })]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "course")
    search_fields = ("title", "course__title")
    list_filter = ("course",)
    inlines = [LessonInline := type('LessonInline', (admin.StackedInline,), {
        'model': Lesson,
        'extra': 1,
    })]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "module", "is_preview")
    search_fields = ("title", "module__title")
    list_filter = ("is_preview", "module")
    inlines = [LessonFileInline, LessonQuizInline]

@admin.register(LessonFile)
class LessonFileAdmin(admin.ModelAdmin):
    list_display = ("lesson", "file_type", "file")
    search_fields = ("lesson__title", "file_type")
    list_filter = ("file_type",)

@admin.register(LessonQuiz)
class LessonQuizAdmin(admin.ModelAdmin):
    inlines = [QuizOptionInline]
    list_display = ('lesson', 'question')
    search_fields = ('lesson__title', 'question')
    list_filter = ('lesson__module__course',)
