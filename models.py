from django.db import models
from django.conf import settings

# Create your models here.
class newsItem(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     title = models.CharField(max_length=100)
     message = models.TextField()
     date_posted = models.DateTimeField()

     def __str__(self):
         return self.title
