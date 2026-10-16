from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from .models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '0.00 $'
        })

        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': f'{datetime.now().date()}'
        })

        self.fields['updated_at'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': f'{datetime.now().date()}'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
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