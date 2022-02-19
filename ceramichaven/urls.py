from django.urls import path
from. import views

app_name = 'ceramichaven'

urlpatterns = [
    path('', views.main_ceramic_page, name='main_page'),
    path('collections/',views.catalog_view, name='catalog_view'),
    path('collections/<slug:collection_slug>/', views.catalog_view,
         name='selected_catalog'),
    path('<int:id>/<slug:product_slug>/', views.product_detail,
         name='product_detail'),



]