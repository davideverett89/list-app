from django.db import models
from .list import List

class ListItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='list')
    
    def __str__(self):
        return self.name