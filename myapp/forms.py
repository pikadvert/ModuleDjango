from django.contrib.auth import authenticate
from django import forms
from django.utils.translation import gettext as _
from django.forms import PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# class AuthenticationForm(forms.Form):
#     username = forms.CharField(max_length=254)
#     password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')
#         if username and password:
#             self.user = authenticate(username=username, password=password)
#             if self.user is None:
#                 raise forms.ValidationError()

class NewUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.wallet = 1000
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()

        return user