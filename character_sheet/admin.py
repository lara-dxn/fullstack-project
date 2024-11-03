from django.contrib import admin
from .models import UserProfile, Character
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Character)