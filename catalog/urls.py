from django.urls import path
from django.views.generic import RedirectView

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=False)),

    path('home/', views.home, name='home'),

    path('contacts/', views.contacts, name='contacts'),

    path('product/<int:pk>/', views.product_item, name='product'),
    path('catalogue/', views.catalogue, name='catalogue'),

]
