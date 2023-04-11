from django import forms
from .models import *

class TalabaForm(forms.Form):
    name=forms.CharField(min_length=3, max_length=30, label='ism')
    course=forms.IntegerField(min_value=1,max_value=7,label='kurs')
    books=forms.IntegerField(min_value=0,max_value=10, label='kitob soni')
    graduate=forms.BooleanField(label='bituruvchi',required=False)


class MuallifForm(forms.Form):
    muallif_ism=forms.CharField(min_length=5,max_length=50,label='muallif ismi')
    hayot=forms.BooleanField(label='hayot',required=False)
    kitoblar=forms.CharField()
    jinsi=forms.ChoiceField(choices=[
        ('Erkak','Erkak'),
        ('ayol','ayol')
    ])
    kitoblar_soni=forms.IntegerField(min_value=0,max_value=10)
    yosh=forms.IntegerField(min_value=10,max_value=91)
    

class RecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields='__all__'
        
        
class AdminForm(forms.ModelForm):
    class Meta:
        model=Admin
        fields='__all__'