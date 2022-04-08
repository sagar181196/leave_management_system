"""leave_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from leave_management_system.account.views import account_leave_approval,account_dashboard,account_add_employee,account_leave,account_add_leave,account_holiday,account_paid_holiday,account_login,logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("account.urls")),
    path('dashboard', account_dashboard),
    path('add_employee',account_add_employee),
    path('leave',account_leave),
    path('add_leave',account_add_leave),
    path('holiday',account_holiday),
    path('paid_holiday',account_paid_holiday),
    path('login',account_login),
    path('logout',logout_view),
    path('approve-leave',account_leave_approval),
    
]
