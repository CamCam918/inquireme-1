from django import forms
from .models import PostModel


class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ["username", "datetimefield", "catergory_verified", "comment"]
