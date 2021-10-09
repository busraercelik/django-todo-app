from django import forms
from .models import Todos

'''
    modele form gonderiyoruz ve bu da db ye gidecek
    normal isteklerde get, form gibi db ye gonderim yapacak isteklerde post kullanılır
'''


class ListForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ['title', 'description', 'date', 'is_finished']
