from django.db import models

class Conference(models.Model):
    location = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    year = models.IntegerField()

    class Meta:
        ordering = ('-year',)
    
# Create your models here.
