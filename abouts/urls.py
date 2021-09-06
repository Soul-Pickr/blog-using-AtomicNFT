from django.urls import path

from . import views

urlpatterns =[
    path('blog',views.blog,name='blog'),
    path('add_blog',views.add_blog,name='add_blog'),
    path('add_blog_content',views.add_blog_content,name='add_blog_content'),
    path('contact',views.contact,name='contact'),
    path('touch',views.touch,name='touch'),
    path('reading/<int:id>/',views.reading,name='reading')
]