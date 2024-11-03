from django.shortcuts import render
from django.views import generic
from .models import Character, UserProfile

class CharacterList(generic.ListView):
    queryset = Character.objects.all()
    template_name = "character_sheet/index.html"
    paginate_by = 6