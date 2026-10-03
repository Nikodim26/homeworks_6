from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.db import connection


class Command(BaseCommand):
    help = 'Добавление данных в базу'

    with connection.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE catalog_product RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;")

    def handle(self, *args, **kwargs):

        categories = [
            {'name': 'Мобильные телефоны', 'description': 'Хорошие телефоны'},
            {'name': 'Стационарные телефоны', 'description': 'Хорошие телефоны'},
            {'name': 'Планшеты', 'description': 'Хорошие планшеты'},
        ]

        for category in categories:
            ctg, created = Category.objects.get_or_create(**category)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added category: {ctg.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {ctg.name}'))


        products = [
            {'name': 'Планшет1', 'description': 'Хороший планшет', 'category_id': 3, 'price': 500.00,
             'created_at': '2000-05-10', 'updated_at': '2010-05-10'},
            {'name': 'Планшет2', 'description': 'Хороший планшет', 'category_id': 3, 'price': 400.00,
             'created_at': '2010-05-10', 'updated_at': '2020-05-10'},
            {'name': 'Планшет1', 'description': 'Хороший планшет', 'category_id': 1, 'price': 300.00,
             'created_at': '2020-05-10', 'updated_at': '2026-05-10'}
        ]

        for product in products:
            prd, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {prd.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {prd.name}'))