from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        verbose_name = kwargs.pop('verbose_name', None)
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control border border-primary border-2 custom-placeholder',
            'placeholder': 'Введите название продукта'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control border border-info',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-select border border-info  rounded-pill',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control border border-info custom-placeholder',
            'placeholder': '0.00 $'
        })

        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control border border-info custom-placeholder',
            'placeholder': f'{datetime.now().date()}'
        })

        self.fields['updated_at'].widget.attrs.update({
            'class': 'form-control border border-info custom-placeholder',
            'placeholder': f'{datetime.now().date()}'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control border border-warning bg-success p-2 text-dark bg-opacity-25 custom-placeholder',
            'placeholder': 'Опишите продукт',
            'style': 'height: 150px;'
        })

        self.fields['publication'].widget.attrs.update({
            'class': "form-check-input",
            'style': "border: 1px solid #ccc;",

        })

        self.fields['publication'].label = verbose_name

        if user and not user.has_perm('catalog.can_unpublish_product'):
            self.fields['publication'].disabled = True
            self.fields['publication'].help_text = 'Отмена публикации доступна только модераторам'

    class Meta:
        model = Product
        fields = '__all__'

    forbidden_words = [
        "казино", "криптовалюта", "крипта", "биржа",
        "дешево", "бесплатно", "обман", "полиция", "радар"
    ]

    def _check_forbidden_words(self, value):
        if value:
            lower_value = value.lower()
            for word in self.forbidden_words:
                if word in lower_value:
                    raise ValidationError(f"Нельзя использовать слово '{word}'")
        return value

    def clean_name(self):
        return self._check_forbidden_words(self.cleaned_data.get("name"))

    def clean_description(self):
        return self._check_forbidden_words(self.cleaned_data.get("description"))

    def clean_price(self):
        value = self.cleaned_data.get("price")
        if value:
            if value < 0:
                raise ValidationError(f"Цена не может быть отрицательной")
        return value
