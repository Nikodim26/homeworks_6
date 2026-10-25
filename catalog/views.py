from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
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

# CUD
class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog_create_update_form.html'
    success_url = reverse_lazy("catalog:catalogue")
    context_object_name = 'product'

class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog_create_update_form.html'
    context_object_name = 'product'

    def get_success_url(self):
        return self.object.get_absolute_url()

class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = 'catalog_delete_form.html'
    success_url = reverse_lazy("catalog:catalogue")
    context_object_name = 'product'