from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm





class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': "input",
        'type': "email",
        'placeholder': "enter email-id",
    }))


class NewPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(NewPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "input",
        'type': "password",
        'autocomplete': "new-password", 
    }))
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
        'class': "input",
        'type': "password",
        'autocomplete': "new-password",
    }))