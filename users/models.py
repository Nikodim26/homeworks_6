from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='users/image', verbose_name='Аватар', blank=True, null=True)
    phone_number = models.CharField(max_length=15, verbose_name='Телефон',blank=True, null=True)
    country = models.CharField(max_length=50, verbose_name='Страна',blank=True, null=True)
    token = models.CharField(max_length=100, verbose_name="Token", blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
