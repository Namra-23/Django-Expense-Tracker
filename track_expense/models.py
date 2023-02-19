from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name

class User(models.Model):
    name=models.CharField(max_length=100)
    gmail=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    phone=models.IntegerField()
    
    def GetUserByEmail(gmail):
        try:
            return User.objects.get(gmail=gmail)
        except:
            return False