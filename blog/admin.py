
# your_app_name/admin.py
from django.contrib import admin
from .models import Post


# Register your models here.
admin.site.register(Post)

# Admin Site Custimazations
admin.site.site_header = "The Fictional Archive Admin"    # Top-left header
admin.site.site_title = "The Fictional Archive Portal"    # Browser tab title
admin.site.index_title = "Welcome to The Fictional Archive Admin"  # Main page index title