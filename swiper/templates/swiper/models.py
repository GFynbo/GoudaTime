from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import Storage

# Create your models here.
class Picture(models.Model):
    """
    Model to hold multiple pictures for a restaurant.
    """
    name = models.CharField(max_length=100, help_text="Enter the picture name (e.g. Seating Area, or Kitchen)")
    image = models.ImageField(upload_to = 'images/', default = 'images/None/no-img.jpg')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Restaurant(models.Model):
    """
    This model stores the required information pertaining to the restaurant
    """

    name = models.CharField(max_length=100, help_text="Enter the restaurant name (e.g. Santarpio's or Jimmy's Subs)")
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    description = models.TextField(max_length=1000, help_text="Enter a brief description of the restaurant")
    address = models.CharField(max_length=75, help_text='123 Sample St, City ST 90210')

    hours = models.CharField(max_length=200, help_text="Enter the restaurant hours (e.g. M-F 9-5, Sat 12-5, Sun Closed)")
    pictures = models.ManyToManyField(Picture, help_text="Select pictures for this restaurant")

    category = models.CharField(max_length=50, help_text="Enter the general food category (e.g. Mexican, American, Thai, etc)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
