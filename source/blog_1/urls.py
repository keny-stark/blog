"""blog_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_views, name='index'),
    path('article/<int:pk>/', article, name='article'),
    path('article/add/', article_create_view, name='article_create_view'),
    path('edit/<int:pk>/', edit_view, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('delete_more/', delete_more, name='delete_more')
]
