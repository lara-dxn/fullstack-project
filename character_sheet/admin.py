from django.contrib import admin
from .models import UserProfile, Character
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Character)
class CharcterAdmin(SummernoteModelAdmin):

    list_display = ('owner', 'name', 'hp', 'character_class')
    search_fields = ['owner']
    #prepopulated_fields = {'': ('',)}
    #summernote_fields = ('name',)

# Register your models here.
admin.site.register(UserProfile)
#admin.site.register(Character)