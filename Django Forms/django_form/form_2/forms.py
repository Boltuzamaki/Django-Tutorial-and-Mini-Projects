from django import forms
from form_2.models import UserModel

class NewUserForm(forms.ModelForm):
    class Meta():
        model= UserModel
        fields = '__all__'
