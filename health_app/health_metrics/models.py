from django.db import models

# Create your models here.
class Patient(models.Model):  
    pid = models.IntegerField()  
    pname = models.CharField(max_length=100)  
    plast_name = models.CharField(max_length=100) 
    page = models.IntegerField()
    pweight = models.IntegerField()
    pheart_rate = models.IntegerField()
    pspo2 = models.IntegerField()
    pestres = models.CharField(max_length = 100)
    class Meta:  
        db_table = "patient"  