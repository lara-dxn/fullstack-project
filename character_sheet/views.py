from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Character, UserProfile

class CharacterList(generic.ListView):
    queryset = Character.objects.all()
    template_name = "character_sheet/index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_effects'] = [
            ('blinded', 'Blinded'), ('charmed', 'Charmed'), ('deafened', 'Deafened'),
            ('frightened', 'Frightened'), ('grappled', 'Grappled'), ('incapacitated', 'Incapacitated'),
            ('invisible', 'Invisible'), ('paralyzed', 'Paralyzed'), ('petrified', 'Petrified'),
            ('poisoned', 'Poisoned'), ('prone', 'Prone'), ('restrained', 'Restrained'),
            ('stunned', 'Stunned'), ('unconscious', 'Unconscious')
        ]
        return context

def character_detail(request, slug):
    """
    Displays character details

    """

    character = get_object_or_404(Character, slug=slug)
    status_effects = [
        ('blinded', 'Blinded'), ('charmed', 'Charmed'), ('deafened', 'Deafened'),
        ('frightened', 'Frightened'), ('grappled', 'Grappled'), ('incapacitated', 'Incapacitated'),
        ('invisible', 'Invisible'), ('paralyzed', 'Paralyzed'), ('petrified', 'Petrified'),
        ('poisoned', 'Poisoned'), ('prone', 'Prone'), ('restrained', 'Restrained'),
        ('stunned', 'Stunned'), ('unconscious', 'Unconscious')
    ]
    
    context = {
        'character': character,
        'status_effects': status_effects,
    }
    return render(request, 'character_sheet/character_detail.html', context)