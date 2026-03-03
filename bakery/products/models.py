from django.db import models

class Category(models.Model):
    """Model representing a product category."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return str(self.name)
class Product(models.Model):
    """Model representing a product with details and category association."""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
    )

    image = models.ImageField(
        upload_to="products/",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)
