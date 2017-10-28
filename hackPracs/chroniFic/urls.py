from django.conf.urls import  url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^customer', views.customer, name='customer'),
    url(r'^department_list',views.department_list, name='department_list'),
    url(r'^illness_list',views.illness_list, name='illness_list'),
    url(r'^about_us',views.about_us, name='about_us'),
    url(r'^hospital_list', views.hospital_list, name='hospital_list'),
    url(r'^book_appointment/', views.book_appointment, name='book_appointment'),
    url(r'^doctor_login', views.doctor_login, name='doctor_login'),

 ]

