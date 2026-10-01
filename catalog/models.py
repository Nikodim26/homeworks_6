from django.db import models


class Product(models.Model):
    name=models.CharField(max_length=100, verbose_name='Наименование')
    description=
    image=
    category=
    price_per_purchase=
    creation_date=
    last_modified_date=






    first_name =
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ['last_name']


"""
наименование,
описание,
изображение,
категория,
цена за покупку,
дата создания,
дата последнего изменения.
"""