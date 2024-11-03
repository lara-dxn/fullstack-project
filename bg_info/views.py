from django.shortcuts import render
from .models import BgInfo


def bg_info_details(request):
    """
    Renders the BG info page
    """
    bg_info = BgInfo.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "bg_info/bg_info.html",
        {"bg_info": bg_info},
    )