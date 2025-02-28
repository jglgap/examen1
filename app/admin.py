from django.contrib import admin
from .models import Student,Degree
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name","surname","degree")
    list_filter = ("name","surname")
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Student, StudentAdmin)
admin.site.register(Degree)
