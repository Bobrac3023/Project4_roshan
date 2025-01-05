from . import views
from django.urls import path

urlpatterns = [
    path('project4_reservation/', views.PostList.as_view(), name='reservation_app_index.html'),
]