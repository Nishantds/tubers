from django.db import models

# Create your models here.
class ContectHere(models.Model):
    full_name=models.CharField(max_length=100)  
    phone=models.IntegerField(default=None)  
    company_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=100)

    def __str__(self):
        return self.email 