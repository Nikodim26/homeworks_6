from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Добавление данных в базу'

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Category.objects.all().delete()

        categories = [
            {'name': 'Плагины для CMS',
             'description': 'Добавляют формы, улучшают SEO, подключают платёжные системы, ускоряют загрузку страниц'},
            {'name': 'Браузерные расширения',
             'description': 'Блокируют рекламу, переводят страницы, помогают в разработке, сохраняют контент'},
            {'name': 'Аудиоплагины',
             'description': 'Добавляют эффекты, синтезируют звуки, помогают сводить и мастерить треки'},
        ]
        ctg_items=[]
        for category in categories:
            ctg, created = Category.objects.get_or_create(**category)
            ctg_items.append(ctg)
            str_ = 'Категория добавлена:' if created else 'Что-то пошло не так:'
            self.stdout.write(self.style.SUCCESS(f'{str_} {ctg.name}'))

        products = [
            {'name': 'Yoast SEO',
             'image': 'catalog/images/Yoast SEO.png',
             'description': 'Помогает оптимизировать страницы под поисковые системы: подсказывает, как улучшить'
                            ' заголовки, метаописания, плотность ключевых слов.',
             'category': ctg_items[0], 'price': 500.00,
             'created_at': '2000-05-10', 'updated_at': '2010-05-10'},
            {'name': 'WooCommerce',
             'image': 'catalog/images/WooCommerce.png',
             'description': 'Превращает WordPress‑сайт в полноценный интернет‑магазин: добавляет корзину, каталог '
                            'товаров, способы оплаты и доставки.',
             'category': ctg_items[0], 'price': 400.00,
             'created_at': '2010-05-10', 'updated_at': '2020-05-10'},
            {'name': 'uBlock Origin',
             'image': 'catalog/images/uBlock Origin.png',
             'description': 'Лёгкий и эффективный блокировщик рекламы и трекеров: убирает всплывающие окна, баннеры,'
                            ' скрипты слежения.',
             'category': ctg_items[1], 'price': 300.00,
             'created_at': '2020-05-10', 'updated_at': '2026-05-10'},
            {'name': 'LanguageTool',
             'image': 'catalog/images/LanguageTool.png',
             'description': 'Проверяет орфографию, грамматику и стиль текста прямо в браузере: подсвечивает ошибки в'
                            ' формах на сайтах, в почте, в редакторах.',
             'category': ctg_items[1], 'price': 300.00,
             'created_at': '2020-05-10', 'updated_at': '2026-05-10'},
            {'name': 'FabFilter Pro‑C 2',
             'image': 'catalog/images/FabFilter Pro‑C 2.png',
             'description': 'Выравнивает динамику звука: делает тихие части громче, а громкие — не слишком резкими.'
                            ' Подходит для вокала, ударных, баса.',
             'category': ctg_items[2], 'price': 300.00, 'created_at': '2020-05-10', 'updated_at': '2026-05-10'},
            {'name': 'Valhalla Vintage Verb',
             'image': 'catalog/images/Valhalla Vintage Verb.png',
             'description': 'Создаёт эффект пространства: имитирует звучание в комнате, зале или на стадионе.'
                            ' Часто используют, чтобы «посадить» вокал в микс.',
             'category': ctg_items[2], 'price': 300.00, 'created_at': '2020-05-10', 'updated_at': '2026-05-10'}

        ]

        for product in products:
            prd, created = Product.objects.get_or_create(**product)

            str_ = 'Продукт добавлен:' if created else 'Что-то пошло не так:'
            self.stdout.write(self.style.SUCCESS(f'{str_} {prd.name}'))
