from django import forms
from .models import Ngo,Review,Doner

class NgoregForm(forms.ModelForm):
    class Meta:
        model=Ngo
        fields=('reg_no','name','specialization','location','state','city','ngo_logo','address','mobile','description','website')
        status = forms.CharField(widget=forms.HiddenInput())

         