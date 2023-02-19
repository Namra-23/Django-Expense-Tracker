from django.forms import ModelForm
from .models import Expense,User
from django import forms

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name','amount','category')

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('name','gmail','password','phone')

class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('gmail','password')
        
    