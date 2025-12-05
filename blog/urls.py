from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.index,name='home'),
    path('blog/<slug:slug>/', views.detail, name='blog-detail'),
    path('blog/create', views.create, name='blog-create'),
    path('blog/delete/<slug:slug>/', views.delete, name='blog-delete'),
    path('blog/update/<slug:slug>/', views.update, name='blog-update'),
    path('blog/search/', views.search, name='blog-search'),
]