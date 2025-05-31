from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),  # show Homepage
    path('about/', views.about_me, name='about'),  # feedback form
    path('contact/', views.contact_us, name='contact_us'),  # Show contact info
    path('reservation/update/<int:pk>/', views.update_reservation,
         name='update_reservation'),  # Edit your reservations
    path('reservation/confirm_delete/<int:pk>/', views.delete_reservation,
         name='confirm_delete'),  # Cancel your reservations
    path('reservation/form/', views.reservation_form,
         name='reservation_form'),  # Make new reservation
    path('reservation/list/', views.reservation_list,
         name='reservation_list'),  # See all your reservations
]
