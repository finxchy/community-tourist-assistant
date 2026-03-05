from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    image_filename = models.CharField(max_length=200, blank=True, default="")

    def __str__(self):
        return self.name