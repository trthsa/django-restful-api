from django.urls import path
from appname.views import create_device, retrieve_device

urlpatterns = [
    path('devices/', create_device, name='create_device'),
    path('devices/<str:device_id>/', retrieve_device, name='retrieve_device'),
]