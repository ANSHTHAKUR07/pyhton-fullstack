from django.db import models

# Create your models here.



class data(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    To_be_completed = models.DateField()

    def __str__(self):
        return self.title