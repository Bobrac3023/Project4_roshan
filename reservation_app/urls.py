from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='index'), # Homepage
    path('about/', views.about_me, name='about'), # About page
    path('reservation/update/<int:pk>/', views.update_reservation, name='update_reservation'), # Update reservation
    path('reservation/confirm_delete/<int:pk>/', views.delete_reservation, name='confirm_delete'),# Delete reservation
    path('reservation/form/', views.reservation_form, name='reservation_form'),
    path('reservation/list/', views.reservation_list, name='reservation_list'),
        
    ]


