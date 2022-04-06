from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from management.models import Book,User
# Register your models here.
admin.site.register(Book)
admin.site.register(User, UserAdmin)