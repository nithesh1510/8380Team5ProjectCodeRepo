from django import forms
#from .models import Profile
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    phone_number = forms.IntegerField(label='Mobile')
    address = forms.CharField(label='Address')
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email','phone_number','address')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


