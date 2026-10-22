from django.contrib.auth.views import LoginView
from django.urls import path
from django.views.generic import RedirectView

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='users:login', permanent=False), name='root'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

]

