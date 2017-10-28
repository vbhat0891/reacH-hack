from django.contrib import admin

from django.contrib import admin
from .models import Hospital, Department, Specialist, Chronic_disease,Patient


class HospitalList(admin.ModelAdmin):
    list_display = ('hospital_id', 'hospital_name', 'city')
    list_filter = ('hospital_id', 'hospital_name', 'city')
    search_fields = ('hospital_id', 'hospital_name')
    ordering = ['hospital_id']

class DepartmentList(admin.ModelAdmin):
    list_display = ('department_id','department_name')
    list_filter = ('department_id','department_name')
    search_fields = ('department_id','department_name')
    ordering = ['department_id','department_name']

class SpecialistList(admin.ModelAdmin):
    list_display = ('specialist_id','specialist_name','state')
    list_filter = ('specialist_id','specialist_name')
    search_fields = ('specialist_id','specialist_name','state')
    ordering = ['specialist_id','specialist_name']

class Chronic_diseaseList(admin.ModelAdmin):
    list_display = ('chronic_disease_id','symptoms','qanda','disease_desc')
    list_filter = ('chronic_disease_id','symptoms','qanda')
    search_fields = ('chronic_disease_id','symptoms','qanda')
    ordering = ['chronic_disease_id']

class PatientList(admin.ModelAdmin):
    list_display = ('patient_id','first_name','last_name','image_field')
    list_filter =  ('patient_id','first_name','last_name','image_field')
    search_fields =  ('patient_id','first_name','last_name')
    ordering = ['patient_id','first_name']

admin.site.register(Hospital, HospitalList)
admin.site.register(Department,DepartmentList)
admin.site.register(Specialist,SpecialistList)
admin.site.register(Chronic_disease,Chronic_diseaseList)
admin.site.register(Patient,PatientList)
