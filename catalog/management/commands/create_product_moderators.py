from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Создаёт группу модераторов продуктов и назначает права"

    def handle(self, *args, **options):
        group, _ = Group.objects.get_or_create(name="Модератор продуктов")

        permissions = Permission.objects.filter(
            content_type__app_label="catalog",
            content_type__model="product",
            codename__in=["can_unpublish_product", "delete_product"],
        )

        if permissions.count() != 2:
            raise CommandError(
                "Не найдены права can_unpublish_product и delete_product. "
                "Сначала выполни миграции."
            )

        group.permissions.set(permissions)
        self.stdout.write(
            self.style.SUCCESS("Группа «Модератор продуктов» создана")
        )