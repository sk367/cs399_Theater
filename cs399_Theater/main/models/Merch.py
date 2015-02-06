from django.db import models

class Merch(models.Model):
	item = models.CharField(default="", max_length = 100)
	price = models.DecimalField(max_digits = 5, decimal_places = 2)
	#picture = models.ImageField(height_field=50, width_field=50)