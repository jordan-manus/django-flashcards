from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# We haven't modified this page yet, fields may need some adjusting-- first name, last name, email

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")