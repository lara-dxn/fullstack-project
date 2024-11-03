from . import views
from django.urls import path

urlpatterns = [
    path('', views.bg_info_details, name='bg_info'),
]