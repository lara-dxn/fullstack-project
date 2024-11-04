from django import forms
from allauth.account.forms import SignupForm
from .models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name', 'hp', 'character_class', 'character_race',
            'blinded', 'charmed', 'deafened', 'frightened', 'grappled',
            'incapacitated', 'invisible', 'paralyzed', 'petrified', 'poisoned',
            'prone', 'restrained', 'stunned', 'unconscious', 'exhaustion'
        ]

class CustomSignupForm(SignupForm):
    isPlayer = forms.BooleanField(required=False, label="Are you a Player?")
    isGM = forms.BooleanField(required=False, label="Are you a GM?")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        # Create the UserProfile and save `isPlayer` and `isGM` fields
        user_profile = user.userprofile
        user_profile.isPlayer = self.cleaned_data.get('isPlayer')
        user_profile.isGM = self.cleaned_data.get('isGM')
        user_profile.save()
        return user
