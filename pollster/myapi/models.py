from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=30)
    alias_name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

