from django.db import models


class Transaction_type(models.TextChoices):
        Income = "IN", "Income"
        Expense = "EX", "Expense"
        
class Expense(models.Model):
    title = models.CharField(max_length=255)
    transaction_type = models.CharField(
        max_length = 2,
        choices= Transaction_type.choices,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.transaction_type} | {self.title} > {self.amount}"