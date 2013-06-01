from django.db import models

class HomeCarousel(models.Model):
    name = models.CharField(max_length=50)
    alt = models.CharField(max_length=50)
    descrip = models.CharField(max_length=50)
