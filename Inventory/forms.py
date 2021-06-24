from django import forms
from .models import *


class LaptopsForms(forms.ModelForm):

    class Meta:
        model=Laptop
        fields="__all__"

class DesktopForm(forms.ModelForm):
    class Meta:
        model=Desktop
        fields="__all__"

class MobilesForm(forms.ModelForm):
    class Meta:
        model=Mobiles
        fields="__all__"