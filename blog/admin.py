
# your_app_name/admin.py
from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)