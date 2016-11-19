from django import forms
from app_clinica.models import *

class FormInsereDentista(forms.ModelForm):

    name = forms.CharField(max_length=150, widget=forms.Textarea(attrs={'class':'form-control col-md-7 col-xs-12'}))
    sex = forms.ChoiceField(widget=forms.CheckboxInput(attrs={'class':'flat'}))
    email = forms.EmailField(widget=forms.Textarea(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=10, widget=forms.Textarea(attrs={'class':'form-control','id':'inputSuccess5'}))
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'flat'}))

    class Meta:
        model = Dentista
        fields = '__all__'