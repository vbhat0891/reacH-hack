from django.contrib import admin

from django.contrib import admin
from .models import Hospital, Department, Specialist, FAQ


class HospitalList(admin.ModelAdmin):
    list_display = ('hospital_id', 'hospital_name', 'city')
    list_filter = ('hospital_id', 'hospital_name', 'city')
    search_fields = ('hospital_id', 'hospital_name')
    ordering = ['hospital_id']



admin.site.register(Hospital, HospitalList)
admin.site.register(Department)
admin.site.register(Specialist)
admin.site.register(FAQ)

