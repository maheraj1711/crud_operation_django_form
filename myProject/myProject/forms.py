from django import forms
from myApp.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=customUser
        fields=UserCreationForm.Meta.fields + ('department','city')


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model=customUser
        fields=['username','password']

class teacherForm(forms.ModelForm):

    class Meta:
        model=teacherModel
        fields=['firstname','username','department','city']
        labels={
            'firstname': 'Enter Your Firstname',
            'username': 'Enter Your Username',
            'department': 'Enter Your Department',
            'city': 'Enter Your City',
        }

class studentForm(forms.ModelForm):

    class Meta:
        model=studentModel
        fields=['firstname','username','department','city']
        labels={
            'firstname': 'Enter Your Firstname',
            'username': 'Enter Your Username',
            'department': 'Enter Your Department',
            'city': 'Enter Your City',
        }

class staffForm(forms.ModelForm):

    class Meta:
        model=staffModel
        fields=['firstname','username','department','city']
        labels={
            'firstname': 'Enter Your Firstname',
            'username': 'Enter Your Username',
            'department': 'Enter Your Department',
            'city': 'Enter Your City',
        }


class doctorForm(forms.ModelForm):

    class Meta:
        model=doctorModel
        fields=['firstname','username','department','city']
        labels={
            'firstname': 'Enter Your Firstname',
            'username': 'Enter Your Username',
            'department': 'Enter Your Department',
            'city': 'Enter Your City',
        }


class nurseForm(forms.ModelForm):

    class Meta:
        model=nurseModel
        fields=['firstname','username','department','city']
        labels={
            'firstname': 'Enter Your Firstname',
            'username': 'Enter Your Username',
            'department': 'Enter Your Department',
            'city': 'Enter Your City',
        }


class employeeForm(forms.ModelForm):

    class Meta:
        model=employeeModel
        fields=['firstname','username','department','city']
        labels={
            'firstname': 'Enter Your Firstname',
            'username': 'Enter Your Username',
            'department': 'Enter Your Department',
            'city': 'Enter Your City',
        }