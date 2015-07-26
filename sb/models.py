from django.db import models

class customer(models.Model):
	first_name = models.CharField(max_length=12)
	last_name = models.CharField(max_length=12)
	home_phone = models.CharField(max_length=10, blank=True)
	cell_phone = models.CharField(max_length=10, blank=True)
	email = models.EmailField(max_length=25, blank=True)
	full_address = models.CharField(max_length=25)
	alt_address = models.CharField(max_length=25, blank=True)
	city = models.CharField(max_length=12)
	state = models.CharField(max_length=12)
	zip_code = models.CharField(max_length=5)