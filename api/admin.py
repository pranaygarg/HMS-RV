from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Student)
admin.site.register(AccountDetails)
admin.site.register(Admin)
admin.site.register(Complaints)
admin.site.register(ComplaintFile)
admin.site.register(Counselor)
admin.site.register(Employee)
admin.site.register(Hostel)
admin.site.register(Hostelite)
admin.site.register(KeyPair)
admin.site.register(LocalGuardian)
admin.site.register(Mess)
admin.site.register(NonAdmin)
admin.site.register(Room)
admin.site.register(Supervisor)
admin.site.register(Teacher)