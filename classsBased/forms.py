from django.forms import Form
from django import forms
from .models import Customer
from django.core import validators

def signeithS(values):
    if values[0].lower()=="t":
        raise forms.ValidationError("name can not start with T or t")
class CusAuthForm(forms.ModelForm):
    first_name=forms.CharField(label="Heda Name",help_text="tomar nam ki?")
    #last_name=forms.CharField(validators=[signeithS],error_messages={"required":"bal amr"})
    class Meta:
        model=Customer
        fields="__all__"
        #fields=["last_name","email"]
        labels={'first_name':"First"} 
        help_text={'email':'Enter Your Name'}
        widgets={
            'first_name':forms.TextInput(attrs={'class':"form-control","required":True},),
            'last_name':forms.TextInput(attrs={'class':"form-control","help_text":"abba"})
        }
