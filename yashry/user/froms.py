from .models import custom_user
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']
        placeholders = ['First Name', 'Last Name', 'Email', 'Password']
        for index, fieldname in enumerate(['first_name', 'last_name', 'email', 'password1']):
            self.fields[fieldname].help_text = None
            self.fields[fieldname].required = True
            self.fields[fieldname].label = False
            self.fields[fieldname].widget.attrs['placeholder'] = placeholders[index]

    class Meta(UserCreationForm):
        model = custom_user
        fields = ("first_name", "last_name", 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = custom_user
        fields = ("first_name", "last_name", 'email')


class customAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = ['Email', 'Password']
        for index, fieldname in enumerate(['username', 'password']):
            self.fields[fieldname].help_text = None
            self.fields[fieldname].required = True
            self.fields[fieldname].label = False
            self.fields[fieldname].widget.attrs['placeholder'] = placeholders[index]
