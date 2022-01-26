from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'mainblog'

urlpatterns = [
    # Main post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('create-post/',views.create_post,name='create_post'),
    path('view-profile/',views.view_profile,name='view_profile'),


]
