from django.db import models
from datetime import datetime

# Create your models here.
class Hiretuber(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    tuber_id=models.CharField(max_length=100)
    tuber_name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    message=models.TextField(max_length=100)
    user_id=models.IntegerField(max_length=100)
    created_date=models.DateTimeField(blank=True,default=datetime.now)


    def __str__(self):
        return self.email 