from django.contrib.auth.forms import AuthenticationForm,UsernameField,UserCreationForm,UserChangeForm
from django.contrib.auth.forms import SetPasswordForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _


class UserAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    class Meta:
        models=User
        fields=["username",'password']


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']


class MyUserChangeDetailsForm(UserChangeForm):
    class Meta:
        model=User
        fields="__all__"


class MyUserChangePasswordForm(PasswordChangeForm):
    class Meta:
        model=User
        fields="__all__"

class MyUSersetPasswordForm(SetPasswordForm):
    class Meta:
        model=User
        fields="__all__"