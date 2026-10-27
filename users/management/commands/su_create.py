from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Создание супера'

    def handle(self, *args, **kwargs):
        user=User(email='lr1975@yandex.ru')
        user.set_password('Lroberon24')
        user.is_active=True
        user.is_staff=True
        user.is_superuser=True
        user.save()
