from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    town = models.CharField(max_length=200, blank=True, default="")

    image_filename = models.CharField(max_length=200, blank=True, default="")

    def __str__(self):
        return self.name

class Review(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="reviews")
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.reviewer_name} - {self.place.name}"
    
    # For update commit message to send to GitHub