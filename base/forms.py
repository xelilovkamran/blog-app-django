from django.contrib.auth.forms import UserCreationForm
from .models import User, Blog
from django import forms


class MyUserCreatingForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "username", 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(MyUserCreatingForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control pt-4 pb-2'
        self.fields['username'].widget.attrs['class'] = 'form-control pt-4 pb-2'
        self.fields['email'].widget.attrs['class'] = 'form-control pt-4 pb-2'
        self.fields['password1'].widget.attrs['class'] = 'form-control pt-4 pb-2'
        self.fields['password2'].widget.attrs['class'] = 'form-control pt-4 pb-2'

        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password'
