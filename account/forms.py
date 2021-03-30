from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    email  = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model  = Account
        fields = ('email', 'username', 'password1', 'password2')
        

class AccountAuthenticationForm(forms.ModelForm):
    password=forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model= Account
        fields =('email', 'password')
    
    def clean(self):
        email =self.cleaned_data['email']
        password =self.cleaned_data['password']
        if not authenticate(email=email, password=password):#if authentication gets wrong on email and password credintials
            raise forms.ValidationError("Invalid login")#here this is our non_field_error which is not specific to our any field
    
class AccountUpdateForm(forms.ModelForm):
    
    class Meta:
        model=Account
        fields=('email', 'username')

    def clean_email(self):
        if self.is_valid():
            email=self.cleaned_data['email']#this will get used to ensure the email after it gets valid only
            try:
                account=Account.objects.exclude(pk=self.instance.pk).get(email=email)#checking here that this email already exist in our account database with same credentials
            except Account.DoesNotExist:#and if doesnot found that email so its fine we simply return this new email
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account.email)#otherwise just raise an that its already existed

    def clean_username(self):
        if self.is_valid():
            username=self.cleaned_data['username']#this will get used to ensure the username after it gets valid only
            try:
                account=Account.objects.exclude(pk=self.instance.pk).get(username=username)#checking here that this username already exist in our account database with same credentials
            except Account.DoesNotExist:#and if doesnot found that username so its fine we simply return this new username
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % account.username)#otherwise just raise an that its already existed