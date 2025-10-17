from django.db import models

# Create your models here.
class Expense(models.Model):
    """A single expense record.

    Fields:
    - title: short title or description
    - amount: Decimal stored as a decimal field (2 decimal places)
    - category: category name (optional)
    - date: date of the expense
    - created_at: auto timestamp when record created
    """
    Title = models.CharField(max_length=255)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Category = models.CharField()
    Date = models.DateField()
    Description = models.TextField() #optional
    Created_at = models.DateTimeField(auto_now_add=True) #timestamp

def __str__(self):
        return self.title