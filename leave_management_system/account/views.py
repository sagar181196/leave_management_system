from django.shortcuts import render
from leave_management_system.account.models import User

def account_view(request):
    return render(request, "login.html")

def account_dashboard(request):
    employees = User.objects.all()
    context = {
        'employees' : employees 
    }
    print(employees)
    return render(request,"dashboard.html",context=context)