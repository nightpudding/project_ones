from django.db import models

# Create your models here.
class blog (models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.ImageField( blank = True, upload_to = 'portfolio/images/')
    date = models.DateField()
    url = models.URLField(blank = True)
    
    def __str__(self):
        return self.title #在後台可以看到正常的文章標題
    