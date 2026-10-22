from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='users/image', verbose_name='Аватар', blank=True, null=True)
    phone_number = PhoneNumberField(verbose_name='Телефон')
    country = models.CharField(max_length=50, verbose_name='Страна',blank=True, null=True)
    is_staff = True
    is_active = True
    is_superuser = True

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
