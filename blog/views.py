from django.shortcuts import render
from django.http import HttpResponse
from .models import content
from abouts.models import blog_content
# Create your views here.

def index(request):

    cont1 = content()
    cont1.title = "Welcome To"
    cont1.topic = "Content Writing Services"
    cont1.des = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. "
    
    conts = content.objects.all()
    blogs= blog_content.objects.all()
    return render(request, 'index.html',{'cont1':cont1,'conts': conts ,'blogs':blogs})




