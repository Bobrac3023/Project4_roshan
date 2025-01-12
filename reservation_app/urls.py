from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='index.html'),
    path('', views.PostList.as_view(), name='index.html'),
    path('', views.PostList.as_view(), name='about.html'),
    #path('',views.comment_edit, name='index.html'),
    ]