from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('posts', views.index, name='main_page'),
    # path('group/<slug:slug>/', views.group_posts),
    path('posts/group_list/', views.group_post, name='group_list')
]
