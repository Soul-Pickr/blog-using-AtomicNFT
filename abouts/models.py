from django.db import models
from django.utils import timezone
# Create your models here.

class blog_content(models.Model):

    date=models.DateField(default=timezone.now)
    img1=models.ImageField(upload_to='pics',blank=True)
    heading=models.CharField(max_length=100)
    subheading1=models.CharField(max_length=200,blank=True)
    keypoints1=models.CharField(max_length=300,blank=True)
    desc1=models.TextField(max_length=10000,blank=True)
    img2=models.ImageField(upload_to='pics',blank=True)
    subheading2=models.CharField(max_length=200,blank=True)
    keypoints2=models.CharField(max_length=300,blank=True)
    desc2=models.TextField(max_length=10000,blank=True)
    img3=models.ImageField(upload_to='pics',blank=True)
    subheading3=models.CharField(max_length=200,blank=True)
    keypoints3=models.CharField(max_length=300,blank=True)
    desc3=models.TextField(max_length=10000,blank=True)
    img4=models.ImageField(upload_to='pics',blank=True)
    subheading4=models.CharField(max_length=200,blank=True)
    keypoints4=models.CharField(max_length=300,blank=True)
    desc4=models.TextField(max_length=10000,blank=True)
    img5=models.ImageField(upload_to='pics',blank=True)
    subheading5=models.CharField(max_length=200,blank=True)
    keypoints5=models.CharField(max_length=300,blank=True)
    desc5=models.TextField(max_length=10000,blank=True)
    img6=models.ImageField(upload_to='pics',blank=True)
    subheading6=models.CharField(max_length=200,blank=True)
    keypoints6=models.CharField(max_length=300,blank=True)
    desc6=models.TextField(max_length=10000,blank=True)
    img7=models.ImageField(upload_to='pics',blank=True)
    subheading7=models.CharField(max_length=200,blank=True)
    keypoints7=models.CharField(max_length=300,blank=True)
    desc7=models.TextField(max_length=10000,blank=True)
    img8=models.ImageField(upload_to='pics',blank=True)
    subheading8=models.CharField(max_length=200,blank=True)
    keypoints8=models.CharField(max_length=300,blank=True)
    desc8=models.TextField(max_length=10000,blank=True)
    img9=models.ImageField(upload_to='pics',blank=True)
    subheading9=models.CharField(max_length=200,blank=True)
    keypoints9=models.CharField(max_length=300,blank=True)
    desc9=models.TextField(max_length=10000,blank=True)
    img10=models.ImageField(upload_to='pics',blank=True)
    subheading10=models.CharField(max_length=200,blank=True)
    keypoints10=models.CharField(max_length=300,blank=True)
    desc10=models.TextField(max_length=10000,blank=True)
    img11=models.ImageField(upload_to='pics',blank=True)
    subheading11=models.CharField(max_length=200,blank=True)
    keypoints11=models.CharField(max_length=300,blank=True)
    desc11=models.TextField(max_length=10000,blank=True)
    img12=models.ImageField(upload_to='pics',blank=True)
    subheading12=models.CharField(max_length=200,blank=True)
    keypoints12=models.CharField(max_length=300,blank=True)
    desc12=models.TextField(max_length=10000,blank=True)
    img13=models.ImageField(upload_to='pics',blank=True)
    subheading13=models.CharField(max_length=200,blank=True)
    keypoints13=models.CharField(max_length=300,blank=True)
    desc13=models.TextField(max_length=10000,blank=True)
    img14=models.ImageField(upload_to='pics',blank=True)
    subheading14=models.CharField(max_length=200,blank=True)
    keypoints14=models.CharField(max_length=300,blank=True)
    desc14=models.TextField(max_length=10000,blank=True)
    img15=models.ImageField(upload_to='pics',blank=True)
    subheading15=models.CharField(max_length=200,blank=True)
    keypoints15=models.CharField(max_length=300,blank=True)
    desc15=models.TextField(max_length=10000,blank=True)

class contact_touch(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=500)