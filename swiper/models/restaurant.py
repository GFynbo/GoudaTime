import uuid

from django.db import models
from .picture import Picture


class Restaurant(models.Model):
    """
    This model stores the required information pertaining to the restaurant
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, help_text="Enter the restaurant name (e.g. Santarpio's or Jimmy's Subs)")
    description = models.TextField(max_length=1000, default="A generic restaurant.", help_text="Enter a brief description of the restaurant")
    address = models.TextField(max_length=125, default="Boston, MA", help_text='123 Sample St, City ST 90210')
    location_lat = models.DecimalField(max_digits=9, decimal_places=6, default=40.7128)
    location_lon = models.DecimalField(max_digits=9, decimal_places=6, default=-74.0060)
    hours = models.CharField(max_length=200, help_text="Enter the restaurant hours (e.g. M-F 9-5, Sat 12-5, Sun Closed)")
    pictures = models.ManyToManyField(Picture, help_text="Select pictures for this restaurant")
    category = models.CharField(max_length=50, help_text="Enter the general food category (e.g. Mexican, American, Thai, etc)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.name)
