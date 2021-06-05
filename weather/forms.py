from django.forms import ModelForm, Select
from .models import City 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

cite = ("patna","delhi")
class CityForm(ModelForm):
    class Meta:
        model = City 
        fields = ['name']
        widgets= {'name':Select(attrs={'class':'select','placeholder':'Selcet City'})}

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

       
