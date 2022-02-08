from django.urls import path
from. import views

app_name = 'artgallery'

urlpatterns = [
    path('', views.art_main_page, name='art_list'),

]