# Generated by Django 3.1.2 on 2021-04-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0003_auto_20210412_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='sub_count',
            field=models.CharField(default='exit', max_length=255),
            preserve_default=False,
        ),
    ]
