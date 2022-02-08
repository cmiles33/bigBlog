from django.contrib import admin
from .models import ArtPost
# Register your models here.


@admin.register(ArtPost)
class ArtPost(admin.ModelAdmin):
    list_display = ('name', 'publish')