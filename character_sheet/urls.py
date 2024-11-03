from django.urls import path
from . import views

urlpatterns = [
    path('', views.CharacterList.as_view(), name='home'),
    path('character_detail/<slug:slug>/', views.character_detail, name='character_detail'),
   # path('character_detail/<slug:slug>/comment/', views.character_detail, name='character_comment'),  # Reuse character_detail for posting
]
