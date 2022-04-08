from django.shortcuts import render
from leave_management_system.account.models import User,EmployeeLeave,PaidHoliday
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse



def account_login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            employees = User.objects.all()
            context = {
                'employees' : employees 
            }
            return render(request,"dashboard.html",context=context)
        else:
            return render(request, "login.html")
    return render(request, "login.html")

def account_dashboard(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    employees = User.objects.all()
    context = {
        'employees' : employees 
    }
    return render(request,"dashboard.html",context=context)

def account_add_employee(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    if request.method =='POST':
        # breakpoint()
        b = User(
            username=request.POST['user_name'],
            first_name=request.POST['first_name'],
            # date=request.POST['DOB'],
            email=request.POST['Email']
            )
        b.save()
    return render(request,'add_employee.html')

def account_leave(request):
    if not request.user.is_authenticated:
         return render(request, "login.html")
    if request.user.is_superuser:
        leaves=EmployeeLeave.objects.all()
    else:
        leaves= EmployeeLeave.objects.filter(user_id=request.user)
    context = {
        'leaves' : leaves
    }
    return render(request,'leave.html',context=context)

def account_add_leave(request):
    
    if not request.user.is_authenticated:
        return render(request, "login.html")

    if request.method == 'POST':
        # breakpoint()
        b=EmployeeLeave(
            user_id=request.user.id,
            date_from=request.POST['from_Date'],
            date_to=request.POST['to_Date'], 
            reason=request.POST['reason'], 
            leave_type=request.POST['leave']
            )
        b.save() 
    return render(request,'add_leave.html')


def account_holiday(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    holidays=PaidHoliday.objects.all().order_by('date')
    context = {
        'holidays' : holidays
    }
    return render(request,'holiday.html',context=context)

def account_paid_holiday(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    if request.method == 'POST':
        # b = PaidHoliday(holiday=request.POST['holiday'], date=request.POST['date'])
        # b.save()
        PaidHoliday.objects.create(
            holiday=request.POST['holiday'], date=request.POST['date']
        )
    return render(request,'paid_holiday.html')



def logout_view(request):
    logout(request)
    return render(request, "login.html")

def account_leave_approval(request):
    EmployeeLeave.objects.filter(id=request.GET['leave_id']).update(is_approved_key=True)
    return HttpResponse(content={'success':True})
    