from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].label = 'Пароль'
        self.fields['password'].widget.attrs.update({'class': 'form-control border border-primary', })
        self.fields['username'].widget.attrs.update({'class': 'form-control border border-primary', })


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].label = 'Пароль'
        self.fields['password1'].help_text = None
        self.fields['password2'].label = 'Повторите пароль'
        self.fields['password2'].help_text = None

        for fild in ['email', 'password1', 'password2', 'avatar', 'phone_number', 'country']:
            self.fields[fild].widget.attrs.update({'class': 'form-control border border-primary', })

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2', 'avatar', 'phone_number', 'country')
