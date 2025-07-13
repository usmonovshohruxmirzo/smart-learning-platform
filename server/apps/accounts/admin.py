from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import StudentModel

@admin.register(StudentModel)
class StudentModelAdmin(BaseUserAdmin):
    ordering = ('email',)
    list_display = ('email', 'full_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'full_name', 'phone_number')

    fieldsets = (
        (None, {'fields': ('email', 'password', 'full_name', 'bio', 'avatar', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'bio', 'avatar', 'phone_number', 'is_active', 'is_staff')}
        ),
    )

    filter_horizontal = ('groups', 'user_permissions',)
