from django.db import models
from .list import List

class ListItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='list')
    
    def __str__(self):
        return self.name