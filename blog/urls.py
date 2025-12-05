from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('create', views.create, name='blog-create'),
    path('delete/<slug:slug>/', views.delete, name='blog-delete'),
    path('update/<slug:slug>/', views.update, name='blog-update'),
    path('search/', views.search, name='blog-search'),
    path('account/', views.account_dashboard, name='account-dashboard'),
    path('<slug:slug>/', views.detail, name='blog-detail'),
]