from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'food'),
        ('Transport', 'transport'),
        ('Bills', 'bills'),
        ('Shopping', 'shopping'),
        ('Health', 'health'),
        ('Others', 'others'),
    ]
    
    user = models.ForeignKey(to=User,on_delete=models.CASCADE) # Cascade deletes the users expenses once the user is being deleted
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=150, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.category}: {self.title} - {self.amount}"
    