from django.db import models
from django.utils import timezone


class Hospital(models.Model):
    hospital_id = models.CharField(primary_key=True,max_length=100)
    hospital_name = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.hospital_id)


class Department(models.Model):
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE,default='')
    department_id = models.CharField(primary_key=True,max_length=100)
    department_name = models.CharField(max_length=200)
    updated_date = models.DateField(default=timezone.now, blank=True, null=True)


    def created(self):
        self.save()

    def updated(self):
        self.save()

    def __str__(self):
        return str(self.department_id)


class Specialist(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE,default='')
    specialist_id= models.CharField(primary_key=True,max_length=100)
    specialist_name=models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.specialist_id)


class FAQ(models.Model):
    specialist=models.ForeignKey(Specialist)
    dep =models.ForeignKey(Department,on_delete=models.CASCADE,default='')
    faq_id=models.CharField(blank=False, null=False,max_length=100)
    questions=models.TextField(max_length=50)
    answers=models.TextField(max_length=50)


