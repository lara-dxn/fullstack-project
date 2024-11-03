from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Character, UserProfile, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden

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

@login_required
def character_detail(request, slug):
    character = get_object_or_404(Character, slug=slug)
    user_profile = UserProfile.objects.get(user=request.user)
    status_effects = [
        ('blinded', 'Blinded'), ('charmed', 'Charmed'), ('deafened', 'Deafened'),
        ('frightened', 'Frightened'), ('grappled', 'Grappled'), ('incapacitated', 'Incapacitated'),
        ('invisible', 'Invisible'), ('paralyzed', 'Paralyzed'), ('petrified', 'Petrified'),
        ('poisoned', 'Poisoned'), ('prone', 'Prone'), ('restrained', 'Restrained'),
        ('stunned', 'Stunned'), ('unconscious', 'Unconscious')
    ]
    comments = Comment.objects.filter(character=character)

    # Check if the user is the owner or a GM to allow comments
    can_comment = user_profile == character.owner or user_profile.isGM

    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if not can_comment:
            return HttpResponseForbidden("You do not have permission to comment.")
        if form.is_valid():
            comment = form.save(commit=False)
            comment.character = character
            comment.user = request.user
            comment.save()
            return redirect('character_detail', slug=character.slug)

    context = {
        'character': character,
        'status_effects': status_effects,
        'comments': comments,
        'form': form,
        'can_comment': can_comment,
    }
    return render(request, 'character_sheet/character_detail.html', context)
