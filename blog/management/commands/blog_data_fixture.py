from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Загружает фикстуру blog_fixture.json для моделей блога'

    def add_arguments(self, parser):
        parser.add_argument(
            '--fixture',
            type=str,
            default='blog_fixture.json',
            help='Путь к файлу фикстуры (по умолчанию: blog_fixture.json)'
        )
        parser.add_argument(
            '--ignore',
            action='store_true',
            help='Игнорировать ошибки по несуществующим объектам (--ignorenonexistent)'
        )

    def handle(self, *args, **options):
        fixture_path = options['fixture']

        if not os.path.isfile(fixture_path):
            self.stdout.write(self.style.ERROR(f'Файл фикстуры не найден: {fixture_path}'))
            return

        self.stdout.write(self.style.WARNING(f'Начинаю загрузку фикстуры: {fixture_path}'))

        try:
            call_command('loaddata', fixture_path, ignore=options['ignore'])
            self.stdout.write(self.style.SUCCESS('Фикстура успешно загружена!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при загрузке фикстуры: {e}'))
            raise
