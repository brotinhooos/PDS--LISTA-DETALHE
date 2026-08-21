from django.db import models

# Create your models here.

class produto (models.Model):
    nome=models.CharField(max_length=50)
    idade=models.IntegerField()
    email=models.EmailField(max_length=254)
    
    def  __str__(self):
        return self.name
    
