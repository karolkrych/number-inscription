from django import forms
from django.core.exceptions import ValidationError

from core.utils import NumberInscriptionBuilder


class NumberInscriptionForm(forms.Form):
    number = forms.CharField(required=True)

    def clean_number(self):
        number = self.cleaned_data['number']
        try:
            int(number)
        except ValueError:
            raise ValidationError('You can type digits only')
        if len(number) > NumberInscriptionBuilder.max_numbers():
            raise ValidationError('The number can be up to 15 characters long')
        return number
