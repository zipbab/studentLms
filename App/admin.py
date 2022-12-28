from django.contrib import admin
from App.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email','dateofbirth','gender', 'grade']
    search_fields = ['name', 'phone', 'email','dateofbirth','gender', 'grade']
    list_per_page = 8

admin.site.register(Student, StudentAdmin)