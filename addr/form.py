from django import forms

from .models import Addr

class AddrForm(forms.ModelForm):

    class Meta:
        model = Addr
        fields = ('author', 'name', 'phone1', 'phone2', 'email',)