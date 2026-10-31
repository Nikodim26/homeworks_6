from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class HomeView(TemplateView):
    template_name = 'home.html'


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'


class CatalogueView(ListView):
    model = Product
    template_name = 'catalogue.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(publication=True)


# CUD
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog_create_update_form.html'
    success_url = reverse_lazy("catalog:catalogue")
    context_object_name = 'product'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['verbose_name'] = 'Опубликовать'
        return kwargs

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog_create_update_form.html'
    context_object_name = 'product'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['verbose_name'] = 'Опубликован'
        return kwargs

    def get_success_url(self):
        return self.object.get_absolute_url()

    # def dispatch(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     if not (self.object.owner == request.user or request.user.is_superuser):
    #         return render(request, 'permission_denied.html', {
    #             'message': 'Не тобой создано - не тебе и изменять',
    #             'product': self.object,
    #         })
    #     return super().dispatch(request, *args, **kwargs)



class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog_delete_form.html'
    success_url = reverse_lazy("catalog:catalogue")
    context_object_name = 'product'
    permission_required = 'catalog.delete_product'

    def handle_no_permission(self):
        return render(
            self.request,
            'permission_denied.html',
            {'message': 'Удаление разрешено только модераторам.'},
            status=403,
        )

    # def dispatch(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     if not (self.object.owner == request.user or request.user.is_superuser):
    #         return render(request, 'permission_denied.html', {
    #             'message': 'Не тобой создано - не тебе и удалять',
    #             'product': self.object,
    #         })
    #     return super().dispatch(request, *args, **kwargs)