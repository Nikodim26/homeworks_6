from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import Product


class HomeView(TemplateView):
    template_name = 'home.html'

class ContactsView(TemplateView):
    template_name = 'contacts.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'

class CatalogueView(ListView):
    model = Product
    template_name = 'catalogue.html'
    context_object_name = 'products'