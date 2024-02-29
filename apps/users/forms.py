from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, ImageField, Form, CharField, PasswordInput, TextInput

from apps.users.models import User

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=28, widget=forms.TextInput(
        attrs={"id": "password", "type": "password"}))
    password2 = forms.CharField(max_length=28, widget=forms.TextInput(
        attrs={"id": "password", "type": "password"}))
    avatar = forms.FileField()

    def save(self, commit=True):
        user = super().save(commit)
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 == password2:
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError("Passwords must be match")

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2", "email", "avatar")

class UserLoginForm(Form):
    username = CharField(max_length=128)
    password = CharField(max_length=128, widget=PasswordInput)
