from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

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

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'blog_create_update_form.html'
    success_url = reverse_lazy("catalog:catalogue")

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'blog_create_update_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()