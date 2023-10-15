from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from manage_hotel.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owner_signup',owner_signup,name="owner_signup"),
   
]