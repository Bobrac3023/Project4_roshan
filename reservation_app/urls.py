from . import views
from django.urls import path

urlpatterns = [
    
    path('workspace/Project4_roshan/reservation_app/templates/reservation/update_reservation.html/', views.update_reservation,
         name='update_reservation.html'), 
    path('', views.about_me, name='index.html'),
    path('', views.PostList.as_view(), name='index.html'),
    path('', views.PostList.as_view(), name='about.html'),
    path('reservation/confirm_delete/<int:pk>/', views.delete_reservation,
         name='confirm_delete'),
 
    ]