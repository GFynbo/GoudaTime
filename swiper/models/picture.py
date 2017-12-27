import uuid

from django.core.files.storage import Storage
from django.db import models


class Picture(models.Model):
    """
    Model to hold multiple pictures for a restaurant.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, help_text="Enter the picture name (e.g. Seating Area, or Kitchen)")
    image = models.ImageField(upload_to = 'swiper/static/img/', default = 'swiper/static/img/no-img.png')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
