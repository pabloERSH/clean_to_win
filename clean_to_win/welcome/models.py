from django.db import models


class GalleryImages(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
