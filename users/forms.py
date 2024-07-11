from django.contrib.auth.forms import UserCreationForm

from email_list.forms import StyleFormMixin
from users.models import User


class UserCreateForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
