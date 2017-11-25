from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = {
            'username',
            'email',
            'password1',
            'password2'
        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class EditProfile(UserChangeForm):

    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'password',
        }
