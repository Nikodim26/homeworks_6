from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from users.models import User
from .models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control border border-primary border-2',
            'placeholder': 'Введите название продукта'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control border border-info',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-select border border-info  rounded-pill',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control border border-info',
            'placeholder': '0.00 $'
        })

        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control border border-info',
            'placeholder': f'{datetime.now().date()}'
        })

        self.fields['updated_at'].widget.attrs.update({
            'class': 'form-control border border-info',
            'placeholder': f'{datetime.now().date()}'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control border border-warning bg-success p-2 text-dark bg-opacity-25',
            'placeholder': 'Опишите продукт',
            'style': 'height: 150px;'
        })


    class Meta:
        model = Product
        fields = '__all__'


    forbidden_words = [
        "казино", "криптовалюта", "крипта", "биржа",
        "дешево", "бесплатно", "обман", "полиция", "радар"
    ]

    def clean_name(self):
        value = self.cleaned_data.get("name")
        if value:
            lower_value = value.lower()
            for word in self.forbidden_words:
                if word in lower_value:
                    raise ValidationError(f"В названии нельзя использовать слово '{word}'")
        return value

    def clean_description(self):
        value = self.cleaned_data.get("description")
        if value:
            lower_value = value.lower()
            for word in self.forbidden_words:
                if word in lower_value:
                    raise ValidationError(f"В описании нельзя использовать слово '{word}'")
        return value

    def clean_price(self):
        value = self.cleaned_data.get("price")
        if value:
            if value < 0:
                raise ValidationError(f"Цена не может быть отрицательной")
        return value