from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.core.exceptions import ValidationError
from django.utils.text import slugify


class User(AbstractUser):
    first_name=models.CharField(max_length=50)
    leave=models.IntegerField(editable=False,default=2,null=True)
     

class PaidHoliday(models.Model):
    holiday=models.CharField(max_length=50)
    date=models.DateField()
   

def present_or_future_date(value):
    if value < datetime.date.today():
        raise ValidationError("The date cannot be in the past!")
    return value


class EmployeeLeave(models.Model):
   
    leave_choices = (
        ('c','casual leave'),
        ('p', 'paid leave')
        )

    date_from=models.DateField(validators=[present_or_future_date])
    date_to=models.DateField(validators=[present_or_future_date])
    reason=models.CharField(max_length=50)
    leave_type=models.CharField(max_length=40,choices=leave_choices)
    is_approved_key=models.BooleanField(default=False ,max_length=50,editable=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE,editable=False)
