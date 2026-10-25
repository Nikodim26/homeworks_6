import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config import settings
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):

    model = User
    form_class = UserRegisterForm
    template_name = 'login_register.html'
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()

        from django.urls import reverse
        url = self.request.build_absolute_uri(
            reverse('users:email-confirm', kwargs={'token': token})
        )

        from django.core.mail import send_mail
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет! Перейди по ссылке, чтобы подтвердить почту: {url}",
            from_email=self.request.META.get('SERVER_NAME', 'no-reply@example.com'),
            recipient_list=[user.email],
            fail_silently=False,
        )

        return super().form_valid(form)


def email_verification(request, token):

    user = get_object_or_404(User, token=token)

    user.is_active = True
    user.token = ''
    user.save()

    return redirect(reverse('users:login'))
