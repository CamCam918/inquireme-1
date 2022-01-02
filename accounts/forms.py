from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, ColorModel
from .models import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'Last_name', 'username',
                                                 'email', 'password', 'birth_date', 'categories_verified', 'coloriqroom')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = UserChangeForm.Meta.fields


class MyModelForm(ModelForm):
    class Meta:
        model = ColorModel
        fields = ['color']
