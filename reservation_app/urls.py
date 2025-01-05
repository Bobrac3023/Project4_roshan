from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='reservation_app_list.html'),
]