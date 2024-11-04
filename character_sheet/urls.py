from django.urls import path
from . import views

urlpatterns = [
    path('', views.CharacterList.as_view(), name='home'),
     path('character/create/', views.character_create, name='character_create'),
    path('character_detail/<slug:slug>/', views.character_detail, name='character_detail'),
    path('character_detail/<slug:slug>/edit/', views.character_edit, name='character_edit'),
    # path('register/', views.register, name='register'),
    # path('characters/', views.character_list, name='character-list'),
    # path('characters/<int:pk>/', views.character_detail, name='character-detail'),
    # path('characters/create/', views.character_create, name='character-create'),
    # path('characters/<int:pk>/update/', views.character_update, name='character-update'),
    # path('characters/<int:pk>/delete/', views.character_delete, name='character-delete'),
]
