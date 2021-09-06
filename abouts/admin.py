from django.contrib import admin
from .models import blog_content, contact_touch

# Register your models here.

admin.site.register(blog_content)

admin.site.register(contact_touch)
