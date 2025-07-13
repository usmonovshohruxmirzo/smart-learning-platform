from django.contrib import admin
from .models import Quiz, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['question']
    inlines = [OptionInline]

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'text', 'is_correct']
