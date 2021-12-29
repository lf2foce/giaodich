from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Username'})
    password.widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Password'})