from django.contrib import admin
from app.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name',)
    fieldsets = (
        ('Personal Information',{
            'fields':(('name','roll_no'),('dob','blood_group'),('father_name','mother_name'),'image')
        }),
        ('Academic Information',{
            'classes':('collapse',),
            'fields':(('sem1_sgpa','sem2_sgpa'),('sem3_sgpa','sem4_sgpa'),('sem5_sgpa','sem6_sgpa'),('sem7_sgpa','sem8_sgpa'), 'avg_sgpa')
        }),
        ('Contact Information',{
            'classes':('collapse',),
            'fields':('phone_number','email')
        })
    )

# Register your models here.

admin.site.register(Student, StudentAdmin)
