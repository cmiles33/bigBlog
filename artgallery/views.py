from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import ArtPost
# Create your views here.


def art_main_page(request):
    artposts = ArtPost.objects.all()

    return render(request, 'artlist.html',
                  {'artposts':artposts})


@login_required
@require_POST
def ajax_change_post(request):
    print("Ajax Request Made")
    art_id = request.POST.get('artpostid')
    art_description = request.POST.get('artpostdescript')
    print(art_id)
    print(art_description)

    return JsonResponse({'status': 'ok'})
