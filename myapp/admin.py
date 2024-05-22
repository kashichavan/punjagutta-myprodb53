from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Student
# Register your models here.

@register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','address']
