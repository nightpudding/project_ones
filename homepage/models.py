from django.db import models


# Create your models here.
class project(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'portfolio/images/')
    url = models.URLField(blank = True)
    
def __str__(self):
    return self.title
    
