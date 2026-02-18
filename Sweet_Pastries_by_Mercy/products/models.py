from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("cake", "Cake"),
        ("bread", "Bread"),
        ("pastry", "Pastry"),
        ("cookie", "Cookie"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)
