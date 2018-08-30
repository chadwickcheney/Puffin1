from django.forms import ModelForm, TextInput
from .models import Site

class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = ['address']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Site'})}
