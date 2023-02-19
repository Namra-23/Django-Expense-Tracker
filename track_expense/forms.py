from django.forms import ModelForm
from .models import Expense,User

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name','amount','category')

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('name','gmail','password','phone')
        
    