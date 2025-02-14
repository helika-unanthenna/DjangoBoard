from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    address = models.CharField(max_length=100)
    additional_details = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    