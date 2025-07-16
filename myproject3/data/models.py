from django.db import models

# Create your models here.



# Model for Services offered by the clinic
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def _str_(self):
        return self.name

# Model for Patients
class Patient(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.full_name