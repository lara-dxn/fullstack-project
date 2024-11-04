from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils.text import slugify
from .models import Character, UserProfile
from .forms import CharacterForm
from django.contrib.auth.decorators import login_required

@login_required
def character_create(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.owner = request.user.userprofile

            # Generate a unique slug
            base_slug = slugify(character.name)
            unique_slug = base_slug
            count = 1
            while Character.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{count}"
                count += 1
            character.slug = unique_slug

            character.save()
            return redirect("character_detail", slug=character.slug)
    else:
        form = CharacterForm()

    return render(request, "character_sheet/character_create.html", {"form": form})


@login_required
def character_edit(request, slug):
    character = get_object_or_404(Character, slug=slug)

    # Check permissions: only the owner, a GM, or an admin can edit
    if request.user != character.owner.user and not request.user.is_staff and not request.user.userprofile.isGM:
        raise PermissionDenied

    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect('character_detail', slug=character.slug)
    else:
        form = CharacterForm(instance=character)

    return render(request, 'character_sheet/character_edit.html', {'form': form, 'character': character})


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

    context = {
        'character': character,
        'status_effects': status_effects,
    }
    return render(request, 'character_sheet/character_detail.html', context)
