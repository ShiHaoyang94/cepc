from django.urls import path

from index import views

urlpatterns = [



    path('',views.index),
    path('<str:name>',views.indexs),
    path('tiyu/<str:name>/',views.tiyu),
    path('douyin/jiexi/',views.douyin),

]
