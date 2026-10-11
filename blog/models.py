from django.db import models


class BlogEntry(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование записи')
    content = models.TextField(verbose_name="Содержание записи", blank=True, null=True)
    preview = models.ImageField(upload_to='blog/image', verbose_name='Превью записи', blank=True, null=True)
    created_at = models.DateField(verbose_name='Дата создания записи')

    publication = models.BooleanField(default=False, verbose_name='Опубликовано')
    number_of_views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'опубликовано {self.number_of_views} раз.'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        ordering = ['created_at', 'name', 'number_of_views']
