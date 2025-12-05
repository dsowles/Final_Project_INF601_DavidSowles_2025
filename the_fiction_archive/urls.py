"""
URL configuration for the_fiction_archive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from blog import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Route for the admin site, using Django's default admin URLs
    path('admin/', admin.site.urls),
    # Route for all URLs starting with 'accounts/',
    # which delegates handling to the 'accounts' app's urls.py file
    path('accounts/', include('accounts.urls')),

    # Route for the root URL (''), which directs requests to the 'index' view function
    # from the 'blog' app. The 'name="home"' provides a simple way to refer to this URL
    # path programmatically in Django code.
    path('', views.index, name='home'),
    path('blog/', include('blog.urls')),
]
