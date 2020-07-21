from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'dashboard/index.html')

def account(request):
    return render(request, 'dashboard/company_details.html')

def edit_offer(request):
    return render(request, 'dashboard/edit_offer.html')

def add_offer(request):
    return render(request, 'dashboard/add_offer.html')

def register(request):
    return render(request, 'dashboard/register.html')

def login(request):
    return render(request, 'dashboard/login.html')

def enterPassword(request):
    return render(request, 'dashboard/enterPassword.html')
