"""
URL configuration for SportsApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from .views.CommentView import CommentView
from .views.ImageView import ImageView
from .views.PostView import PostView

urlpatterns = [
    path('get-comments', CommentView.as_view()),
    path('get-images', ImageView.as_view()),
    path('get-posts', PostView.as_view()),
]
