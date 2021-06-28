from django.db import models

# Create your models here.
class blog (models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'portfolio/images/')
    date = models.DateField()
    url = models.URLField(blank = True)