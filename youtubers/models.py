from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):
    crew_choices=(
        ('solo','solo'),
        ('small','small'),
        ('large','large'),    )

    camera_choices=(
        ('canon','canon'),
        ('nikon','nikon'),
        ('soney','soney'),
        ('red','red'),
        ('fuji','fuji'),
        ('panasonic','panasonic'),
        ('other','other'),
    )    
    
    categroy_choice=(
        ('code','code'),
        ('mobile_review','mobile_review'),
        ('vlogs','vlogs'),
        ('comedy','comedy'),
        ('gaming','gaming'),
        ('film_making','film_making'),
        ('cooking','cooking'),
        ('other','other'),
    )    


    name=models.CharField(max_length=255)
    price=models.IntegerField()
    photo=models.ImageField(upload_to='media/ytubers/%Y/%m/')
    video_url=models.CharField(max_length=255)
    description=RichTextField(max_length=2555)
    city=models.CharField(max_length=255)
    age=models.CharField(max_length=255)
    height=models.CharField(max_length=255)
    crew=models.CharField( choices=crew_choices,max_length=255)
    camera_type=models.CharField(choices=camera_choices,max_length=255)
    sub_count=models.CharField(max_length=255,default='')
    category=models.CharField(choices=categroy_choice,max_length=255)
    is_featured=models.BooleanField(default=False)
    created_date=models.DateTimeField(default=datetime.now,blank=True)