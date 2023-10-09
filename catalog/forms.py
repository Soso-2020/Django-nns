from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({"class": 'login_reg'})
        self.fields['email'].widget.attrs.update({'class': 'login_reg'})
        self.fields['password1'].widget.attrs.update({'class': 'password_reg'})
        self.fields['password2'].widget.attrs.update({'class': 'password_reg'})
    username = forms.CharField()
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class CommentForm(forms.Form):
    comment = forms.CharField()