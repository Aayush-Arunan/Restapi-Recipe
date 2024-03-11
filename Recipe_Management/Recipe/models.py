from django.db import models

# Create your models here.

class Cuisine(models.Model):
    Title=models.CharField(max_length=30)
    Meal=models.CharField(max_length=30)
    Ingredients=models.CharField(max_length=30)
    Rating=models.IntegerField()
    Review=models.CharField(max_length=100)

    def __str__(self):
        return self.Title