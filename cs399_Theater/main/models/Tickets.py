from django.db import models

class Tickets(models.Model):
  name = models.CharField(max_length=128, default="")
  date = models.DateTimeField()
  available = models.IntegerField()
