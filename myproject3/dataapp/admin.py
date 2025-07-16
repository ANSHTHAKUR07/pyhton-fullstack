from django.contrib import admin
from .models import Service, Patient, Doctor , Intern , Appointment , Feedback , Treatment
# Register your models here.


admin.site.register(Service)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Intern)
admin.site.register(Appointment)
admin.site.register(Treatment)
admin.site.register(Feedback)