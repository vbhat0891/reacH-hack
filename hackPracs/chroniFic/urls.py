from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^customer',views.customer, name='customer'),
    url(r'^department_list',views.department_list, name='department_list'),
    url(r'^illness_list',views.illness_list, name='illness_list'),
    url(r'^about_us',views.about_us, name='about_us'),

 ]


