from django import forms
from django.core.exceptions import ValidationError

from .models import Product

class ProductForm(forms.ModelForm):
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