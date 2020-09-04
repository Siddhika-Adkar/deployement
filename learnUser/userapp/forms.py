from django import forms

from .models import UserProfileInfo,User
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')
        #fields='__all__'

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')