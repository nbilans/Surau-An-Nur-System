from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    Userid = forms.CharField(label="", max_length=15, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ID'}))
    Username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    Useremail = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    Userphone = forms.CharField(label="", max_length=12, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone No'}))

    class Meta:
        model = User
        fields = ('Userid', 'Username', 'username', 'Useremail', 'Userphone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''


class EmpSignUpForm(UserCreationForm):
    Employeeid = forms.CharField(label="", max_length=15, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ID'}))
    Employeename = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    Employeephone = forms.CharField(label="", max_length=12, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone No'}))

    class Meta:
        model = User
        fields = ('Employeeid', 'Employeename', 'username', 'Employeephone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(EmpSignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''

