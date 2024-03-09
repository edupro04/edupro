from  django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, \
    PasswordChangeForm


User = get_user_model()


class MyAuthenticationForm(AuthenticationForm):
   username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','name':'email or phone','placeholder':'Email Address or phone','id':'inputEmail'}),required=True)
   password =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','id':'inputPassword','name':'password'}),required=True)

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name','id':'fname',}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name','id':'lname',}),required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address','id':'uemail',}),required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'create password','id':'inputPassword1',}),required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm password', 'id': 'inputpassword2', }), required=True)
    phone = forms.RegexField(regex=r'^[6-9]\d{9}$',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mobile number', 'id': 'mobile', }), required=True)
    city= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address','id':'address',}),required=True)
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'phone',
            'city',
            }
        exclude = {'username'}

    def save(self, commit=True):
        user = super(RegistrationForm,self).save(commit = False)
        user.username=self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']


        if commit:
            user.save()

        return user


class PasswordChangeForm(PasswordChangeForm):
    old_password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'old password','id':'oldPassword'}) ,required=True)
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'new password', 'id': 'newPassword'}), required=True)
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'confirm new password', 'id': 'newconfirmPassword'}), required=True)


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email Address', 'id': 'uemail'}) ,required=True)
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'First Name', 'id': 'uemail', }),required=True,)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Last Name', 'id': 'uemail', }),required = True)
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'id': 'address', }),
        required=True)
    phone = forms.RegexField(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}$', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter mobile number', 'id': 'mobile', }), required=True)


    class Meta:
        model = User
        fields = {
            'email',
            'first_name',
            'last_name',
            'city',
            'phone',
        }
        exclude = {

        }
        #we can use exclude = {}
class NewPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder': 'Email Address', 'id': 'email', }),required=True)
