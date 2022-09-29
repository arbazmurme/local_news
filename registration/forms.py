from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class UserRagistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput( attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput( attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }

class UserLoginForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=254)
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class EditProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email' )