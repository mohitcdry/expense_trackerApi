from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ExpenseIncome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10, choices=[("credit", "credit"), ("debit", "debit")]
    )
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_type = models.CharField(
        max_length=10,
        choices=[("flat", "flat"), ("percentage", "percentage")],
        default="flat",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
