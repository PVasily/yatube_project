from django.urls import path
from . import views


urlpatterns = [
    path('posts', views.index),
    path('group/<slug:slug>/', views.group_posts)
]
