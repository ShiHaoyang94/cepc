from django.urls import path

from trip_card_records import views

urlpatterns = [



    path('post/',views.post),


]
