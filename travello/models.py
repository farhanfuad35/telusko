from django.db import models

# Create your models here.
# Create the class. But instantiate in the views

class Destination(models.Model):		# Use models.Model when you want to make the class a model to be used in database
	name = models.CharField(max_length=100) # Use = instead of : in regular class
	img = models.ImageField(upload_to='pics')	# In media/pics
	desc = models.TextField(default='')
	price = models.IntegerField(default=0)
	offer = models.BooleanField(default=False)