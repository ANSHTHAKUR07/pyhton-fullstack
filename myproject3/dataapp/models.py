from django.db import models

# Create your models here.



# Model for Services offered by the clinic
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

# Model for Patients
class Patient(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Doctor(models.Model):
    full_name = models.CharField(max_length=150, unique=True)
    department = models.CharField(max_length=100)
    typeof = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
class Treatment(models.Model):
          full_name = models.CharField(max_length=150, unique=True)
          typeof = models.CharField(max_length=15)
          price = models.CharField(max_length=20)
          created_at = models.DateTimeField(auto_now_add=True)

          def __str__(self):
           return self.full_name
          
class Intern(models.Model):
        full_name = models.CharField(max_length=150, unique=True)
        department = models.CharField(max_length=15)
        email = models.EmailField(unique=True)
        phone = models.CharField(max_length=15)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
           return self.full_name
        
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    treatment = models.ForeignKey(Treatment, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.date} {self.time}"


class Feedback(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
