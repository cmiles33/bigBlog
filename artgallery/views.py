from django.shortcuts import render, get_object_or_404, redirect
from .models import ArtPost
# Create your views here.


def art_main_page(request):

    return render(request, 'artlist.html')
