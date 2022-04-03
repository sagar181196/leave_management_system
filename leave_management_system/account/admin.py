from django.contrib import admin
from .models import PaidHoliday,EmployeeLeave,User
from django.db.models import F


@admin.action(description='Approve Leaves')
def approve_leaves(modeladmin, request, queryset):
    # User.objects.filter(id=request.user.id).update(leave=F('leave')-1)
    queryset.update(is_approved_key=True)
    for q in queryset:
        q.user.leave = q.user.leave - 1
        q.user.save()


class useradmin(admin.ModelAdmin):
    list_display=['first_name','leave']


class PaidHolidayadmin(admin.ModelAdmin):
    list_display=('holiday','date')


class EmployeeLeaveadmin(admin.ModelAdmin):
    list_display= ['user','date_from', 'date_to','reason','leave_type','is_approved_key']
    actions = [approve_leaves]

    def get_queryset(self, request):
        if request.user.is_superuser:
            all_entries=EmployeeLeave.objects.all()
        else:
            all_entries = EmployeeLeave.objects.filter(user=request.user)
        return all_entries

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    



admin.site.register(User,useradmin)
admin.site.register(PaidHoliday,PaidHolidayadmin)
admin.site.register(EmployeeLeave,EmployeeLeaveadmin)