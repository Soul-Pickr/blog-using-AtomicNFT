# Generated by Django 3.2.3 on 2021-05-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abouts', '0005_auto_20210522_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_content',
            name='img1',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
