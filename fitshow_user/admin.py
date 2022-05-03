from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

UserAdmin.fieldsets[1][1]["fields"] = ("first_name", "last_name", "phone", "age", "national_code", "email", "course_duration")

admin.site.register(User, UserAdmin)