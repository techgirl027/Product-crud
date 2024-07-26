from django.db import models
from django.db import models
from random import sample
import string


class GenereteCode(models.Model):
    generate_code = models.CharField(max_length=255, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.generate_code:
            self.generate_code = "".join(sample(string.ascii_letters, 20))
        super(GenereteCode, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Category(GenereteCode):
    name = models.CharField(max_length=255)
    img = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(GenereteCode):
    name: str = models.CharField(max_length=255)
    quantity: int = models.PositiveIntegerField(default=1)
    price: float = models.DecimalField(max_digits=8, decimal_places=2)
    # category: Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description: str = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductEnter(GenereteCode):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantitiy = models.IntegerField()
    old_quantity = models.IntegerField(blank=True)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.product.name

    def save(self, *args, **kwargs):
        if not self.generate_code:
            self.old_quantity = self.product.quantity
            self.product.quantity = self.quantitiy
        else:
            self.product.quantity -= ProductEnter.objects.get(
                generate_code=self.generate_code
            ).quantitiy
            self.product.quantity += self.quantitiy
        self.product.save()
        super(ProductEnter, self).save(*args, **kwargs)
