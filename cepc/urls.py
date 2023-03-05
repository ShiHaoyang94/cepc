"""Note_Cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include


import trip_card_records.views
from trip_card_records import views as index_views
from cepc import view, settings
from abnormal_records import views
from all_user import views as user_views
urlpatterns = [


    path('admin/', admin.site.urls),
    path('all_user/',include('all_user.urls')),
    path('trip_card_records/',include('trip_card_records.urls')),
    path('',view.login),
    path('busy/',user_views.busy),
    path('successful/',user_views.successful),
    path('abnormal_records/',include('abnormal_records.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)