from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarService(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    before_pics = models.ImageField()
    after_pics = models.ImageField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    categories = models.ForeignKey( Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title