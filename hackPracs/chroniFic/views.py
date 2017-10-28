from django.shortcuts import render

# Create your views here.


def home(request):
   return render(request, 'chroniFic/home.html',
                 {'chroniFic': home})


def customer(request):
        return render(request, 'chroniFic/customer.html',
                  {'chroniFic': customer})


def department_list(request):
    return render(request, 'chroniFic/department_list.html',
                  {'chroniFic': department_list})

def illness_list(request):
    return render(request, 'chroniFic/illness_list.html',
                  {'chroniFic': illness_list})


def about_us(request):
    return render(request, 'chroniFic/about_us.html',
                  {'chroniFic': about_us})


def hospital_list(request):
    return render(request, 'chroniFic/hospital_list.html',
                  {'chroniFic': hospital_list})


def book_appointment(request):
    return render(request, 'chroniFic/book_appointment.html',
                  {'chroniFic': book_appointment})