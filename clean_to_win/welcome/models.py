from django.db import models


images_path = "static/welcome/images/"


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=images_path)
    description = models.TextField(blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
