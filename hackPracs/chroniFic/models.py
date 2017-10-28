from django.db import models
from django.utils import timezone
from django.urls import reverse



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
    create_date= models.DateTimeField(default=timezone.now)
    update_date = models.DateField(default=timezone.now, blank=True, null=True)


    def created(self):
        self.create_date = timezone.now()
        self.save()


    def updated(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        self.save()
        return str(self.department_id)


class Specialist(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE,default='')
    specialist_id= models.CharField(primary_key=True,max_length=100)
    specialist_name=models.CharField(max_length=200)
    specialist_details=models.CharField(max_length=200,default='')
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
        self.save()
        return str(self.specialist_id)


class Chronic_disease(models.Model):
    spec = models.ForeignKey(Specialist,on_delete=models.CASCADE,default='')
    dep =models.ForeignKey(Department,on_delete=models.CASCADE,default='')
    chronic_disease_id= models.CharField(primary_key=True,max_length=10)
    disease_desc = models.TextField(default='')
    symptoms = models.TextField()
    qanda=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        self.save()
        return str(self.chronic_disease_id)

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email=models.CharField(max_length=50)
    text_field = models.TextField(max_length=1000)
    image_field = models.FileField()
    created_date =  models.DateTimeField(timezone.now())


    def created(self):
        self.created_date = timezone.now()
        self.save()

        # on submit click on the user entry page, it redirects to the url below.

    def get_absolute_url(self):
        return reverse('chroniFic:home')


    def __str__(self):
        return str(self.patient_id)


