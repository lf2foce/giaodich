from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="User name", max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

