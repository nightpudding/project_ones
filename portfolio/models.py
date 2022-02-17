from django.db import models

# Create your models here.
# 設定網頁顯示內容

class project(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'portfolio/images/')
    url = models.URLField(blank = True)
    
