from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # password1 = forms.CharField(label='Enter password',
    #                             widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Confirm password',
    #                             widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        # help_texts = {
        #     'username': 'This is a test',
        # }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
