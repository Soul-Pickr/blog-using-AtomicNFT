
from django.shortcuts import redirect, render
from .models import blog_content, contact_touch

# Create your views here.
def about(request):    
   return render(request,'about.html')

def blog(request):
    
    blogs= blog_content.objects.all()
    return render(request, 'blog.html',{'blogs':blogs})

def add_blog(request):
    return render(request,'add_blog.html')

def add_blog_content(request):

    
    heading= request.POST['heading']
    subheading1= request.POST['subheading1']
    keypoints1= request.POST['keypoints1']
    desc1=request.POST['desc1']

    
    subheading2= request.POST['subheading2']
    keypoints2= request.POST['keypoints2']
    desc2=request.POST['desc2']

   
    subheading3= request.POST['subheading3']
    keypoints3= request.POST['keypoints3']
    desc3=request.POST['desc3']

    
    subheading4= request.POST['subheading4']
    keypoints4= request.POST['keypoints4']
    desc4=request.POST['desc4']

   
    subheading5= request.POST['subheading5']
    keypoints5= request.POST['keypoints6']
    desc5=request.POST['desc6']

   
    subheading6= request.POST['subheading6']
    keypoints6= request.POST['keypoints6']
    desc6=request.POST['desc6']

    
    subheading7= request.POST['subheading1']
    keypoints7= request.POST['keypoints1']
    desc7=request.POST['desc1']

    
    subheading8= request.POST['subheading8']
    keypoints8= request.POST['keypoints8']
    desc8=request.POST['desc8']

   
    subheading9= request.POST['subheading9']
    keypoints9= request.POST['keypoints9']
    desc9=request.POST['desc9']

    
    subheading10= request.POST['subheading10']
    keypoints10= request.POST['keypoints10']
    desc10=request.POST['desc10']

    
    subheading11= request.POST['subheading11']
    keypoints11= request.POST['keypoints11']
    desc11=request.POST['desc11']

   
    subheading12= request.POST['subheading12']
    keypoints12= request.POST['keypoints12']
    desc12=request.POST['desc12']

   
    subheading13= request.POST['subheading13']
    keypoints13= request.POST['keypoints13']
    desc13=request.POST['desc13']

   
    subheading14= request.POST['subheading14']
    keypoints14= request.POST['keypoints14']
    desc14=request.POST['desc14']

    
    subheading15= request.POST['subheading15']
    keypoints15= request.POST['keypoints15']
    desc15=request.POST['desc15']
    blogs_content=blog_content.objects.create(heading=heading,subheading1=subheading1,keypoints1=keypoints1,desc1=desc1,subheading2=subheading2,keypoints2=keypoints2,desc2=desc2,subheading3=subheading3,keypoints3=keypoints3,desc3=desc3,subheading4=subheading4,keypoints4=keypoints4,desc4=desc4,subheading5=subheading5,keypoints5=keypoints5,desc5=desc5,subheading6=subheading6,keypoints6=keypoints6,desc6=desc6,subheading7=subheading7,keypoints7=keypoints7,desc7=desc7,subheading8=subheading8,keypoints8=keypoints8,desc8=desc8,subheading9=subheading9,keypoints9=keypoints9,desc9=desc9,subheading10=subheading10,keypoints10=keypoints10,desc10=desc10,subheading11=subheading11,keypoints11=keypoints11,desc11=desc11,subheading12=subheading12,keypoints12=keypoints12,desc12=desc12,subheading13=subheading13,keypoints13=keypoints13,desc13=desc13,subheading14=subheading14,keypoints14=keypoints14,desc14=desc14,subheading15=subheading15,keypoints15=keypoints15,desc15=desc15)
    blogs_content.save()
    return render(request,'blog.html')

def contact(request):
    return render(request, 'contact.html')

def touch(request):
     
    name = request.POST['name']
    email = request.POST['email']
    message= request.POST['message']
    contact_touchs=contact_touch.objects.create(name=name,email=email,message=message)
    contact_touchs.save()
    return render(request,'contact.html')
    

def reading(request,id):

    blogs= blog_content.objects.get(id=id)
    return render(request, 'reading.html',{'blogs':blogs})

