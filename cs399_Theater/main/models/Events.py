from django.db import models

class Events(models.Model):
  name = models.CharField(max_length=128, default="")
  date = models.DateTimeField()
  cost = models.DecimalField(max_digits = 5, decimal_places=2)
  genre = models.CharField(max_length=50, default="folk")
  description = models.TextField(default="This band plays music")
  
  
