# Owner Daine.H
# Modify 2016-01-05

from django import forms


class SignUpForm(forms.Form):
    userid = forms.CharField(label='User ID', max_length=32)
    passwd1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    passwd2 = forms.CharField(label='Retype Password', widget=forms.PasswordInput())



class LoginInForm(forms.Form):
    userid = forms.CharField(label='User ID', max_length=32)
    passwd = forms.CharField(label='Password', widget=forms.PasswordInput())