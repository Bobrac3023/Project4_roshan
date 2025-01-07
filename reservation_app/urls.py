from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='reservation_app_index.html'),
    path('', views.PostList.as_view(), name='index.html'),
    #path('sample-cv.pdf', views.PostList.as_view(), name='menucard'),
    #path('', views.PostList.as_view(), name='reservation_app_about.html'),
    #path('project4_reservation/', views.PostList.as_view(), name='index.html'),
]