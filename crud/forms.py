from django import forms
from django.forms import ModelForm
from .models import DB

class viewForm(ModelForm):
    name = forms.CharField(max_length=255, )
    age = forms.IntegerField( )
    email = forms.EmailField( )
    bio = forms.TextInput()
    image = forms.ImageField()


    class Meta:
        model = DB
        fields = ('name', 'age', 'email','bio','image')
        labels = {
            'name': 'Fullname',
            'age': 'Age',
            'email': 'E-mail',
            'bio': 'Bio',
            'image': 'Image'
        }
