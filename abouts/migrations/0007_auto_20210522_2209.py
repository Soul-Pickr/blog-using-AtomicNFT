# Generated by Django 3.2.3 on 2021-05-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abouts', '0006_alter_blog_content_img1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_content',
            name='heading',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blog_content',
            name='img1',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]
