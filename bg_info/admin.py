from django.contrib import admin
from .models import BgInfo
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BgInfo)
class BgInfoAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)