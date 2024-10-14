from django.shortcuts import render


def Home(request):
    return render(request, 'pages/home.html')


def About(request):
    return render(request, 'pages/about.html')


def Departments(request):
    return render(request, 'pages/departments.html')


def Doctors(request):
    return render(request, 'pages/doctors.html')


def Contact_Us(request):
    return render(request, 'pages/contact_us.html')
