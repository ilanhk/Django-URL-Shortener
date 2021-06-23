from .models import ShortURL
from django import forms

class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = {'original_url'}

        # Created a widget to control what html element the form would use.
        widgets = {
            'original_url': forms.TextInput(attrs={'class': 'form-control'}),
            # To make sure the form element has the class 'form-control' because its the bootstrap class we will use.
        }