from django.urls import path
from django.views.generic import RedirectView

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, CatalogueView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='catalog:home', permanent=False), name='root'),
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),

]
