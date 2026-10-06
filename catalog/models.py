from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование товара')
    image = models.ImageField(upload_to='catalog/media', verbose_name='Изображение', help_text='Загрузите картинку',
                              blank=True, null=True)
    category = models.ForeignKey(to='Category', verbose_name='Категория', help_text='Введите категорию товара',
                                 on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text="Укажите цену за одну покупку")
    created_at = models.DateField(verbose_name='Дата изготовления', help_text='Введите дату изготовления товара')
    updated_at = models.DateField(verbose_name='Дата последнего изменения',
                                  help_text='Введите дату последнего изменения товара')
    description = models.TextField(verbose_name="Описание товара", blank=True, null=True,
                                   help_text="Введите подробное описание товара.")

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name', 'price']


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование категории')
    description = models.TextField(verbose_name="Характеристика категории", blank=True, null=True,
                                   help_text="Опишите суть категории товаров")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
