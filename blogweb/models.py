from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    pic = models.ImageField(upload_to='images/', blank=True)
    
    def __str__(self):
        return self.title
