from django.db import models

# Create your models here.
class familiar(models.model):
    nombre= models.CharField(max_length=50)
    edad= models.IntegerField()
    fecha_de_nac= models.DateField()
    