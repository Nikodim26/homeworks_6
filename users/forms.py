from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserLoginForm(UserCreationForm):

    class Meta:
        model = User