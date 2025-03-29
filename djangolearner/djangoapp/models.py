from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.category}"
    
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title