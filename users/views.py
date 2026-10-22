from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserLoginForm
from users.models import User


class ProductCreateView(CreateView):
    model = User
    form_class = UserLoginForm
    template_name = 'catalog_create_update_form.html'
    success_url = reverse_lazy("blog:entries")