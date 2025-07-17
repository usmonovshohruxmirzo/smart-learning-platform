from django.contrib import admin
from .models import Course, Module, Lesson, LessonFile

class LessonFileInline(admin.TabularInline):
    model = LessonFile
    extra = 1

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "instructor", "visibility", "created_at")
    search_fields = ("title", "description", "instructor__email")
    list_filter = ("visibility", "created_at")
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "course")
    search_fields = ("title", "course__title")
    list_filter = ("course",)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "module", "is_preview")
    search_fields = ("title", "module__title")
    list_filter = ("is_preview", "module")
    inlines = [LessonFileInline]

@admin.register(LessonFile)
class LessonFileAdmin(admin.ModelAdmin):
    list_display = ("lesson", "file_type", "file")
    search_fields = ("lesson__title", "file_type")
    list_filter = ("file_type",)
