from django.urls import path
from django.views.generic import RedirectView

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, CatalogueView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='catalog:home', permanent=False), name='root'),
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),

    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),

    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
