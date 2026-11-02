from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    category = models.CharField(max_length=30)
    price = models.DecimalField(max)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name