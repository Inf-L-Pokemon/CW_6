from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from email_list.forms import StyleFormMixin
from users.models import User


class UserCreateForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserUpdateForm(StyleFormMixin, UserChangeForm):
    class Meta:
        exclude = ('token',)


class UserUpdateModeratorForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('is_active',)


class UserForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        exclude = ('token', 'is_active')
