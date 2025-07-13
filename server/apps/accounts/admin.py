from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StudentModel

class StudentModelAdmin(UserAdmin):
    model = StudentModel
    list_display = ('email', 'full_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'full_name', 'phone_number')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'full_name', 'bio', 'avatar', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'bio', 'avatar', 'phone_number', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(StudentModel, StudentModelAdmin)
