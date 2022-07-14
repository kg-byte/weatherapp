from django.forms import ModelForm
from django import forms
from .models import User
class UserForm(ModelForm):
	username = forms.TextInput()
	address = forms.TextInput()
	class Meta:
		model = User
		fields = ['username', 'address']