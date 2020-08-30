"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view(),name='create'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(),name='detail'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(),name='update'),
    path('', views.PostListView.as_view(),name='list'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(),name='delete'),
    path('drafts/', views.PostDraftView.as_view(),name='drafts'),
    path('comments/<int:pk>/', views.CommentCreateView.as_view(),name='comments'),
    path('approve/<int:pk>/', views.ApproveView.as_view(),name='approve'),
    path('publish/<int:pk>/', views.PublishView.as_view(),name='publish'),
    path('about/', views.AboutView.as_view(),name='about'),
]
