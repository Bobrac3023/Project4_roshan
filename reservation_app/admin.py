from django.contrib import admin
from .models import Reservation,Feedback


# Register your models here
admin.site.register(Reservation)
admin.site.register(Feedback)

#@admin.register(Reservation)
#@admin.register(Feedback)
#class ReservationtAdmin(admin.ModelAdmin):

    #list_display = ('message', 'read',)


