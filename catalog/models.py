from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    image = models.ImageField(upload_to='catalog/image', verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey(to='Category', verbose_name='Категория', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата последнего изменения')
    description = models.TextField(verbose_name="Описание продукта", blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.price}'

    def get_absolute_url(self):
        return reverse('catalog:catalogue', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name', 'price']


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name="Характеристика категории", blank=True, null=True
                                   )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
