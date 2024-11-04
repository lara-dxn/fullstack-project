from django.urls import path
from . import views

urlpatterns = [
    path('', views.CharacterList.as_view(), name='home'),
    path('character/create/', views.character_create, name='character_create'),
    path('character_detail/<slug:slug>/', views.character_detail, name='character_detail'),
    path('character_detail/<slug:slug>/edit/', views.character_edit, name='character_edit'),
    path('character_detail/<slug:slug>/delete/', views.character_delete, name='character_delete'),
]
