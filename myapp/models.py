from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext as _

class MyUser(AbstractUser):
    avatar = models.ImageField(blank=True, null=True)
    wallet = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    email = models.EmailField(max_length=150, blank=False, unique=True)

    class Meta:
        verbose_name = _("MyUser")
        verbose_name_plural = _("MyUser")
        ordering = ["username"]

    def __str__(self):
        return self.username

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to="images/")
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["product_name"]

    def __str__(self):
        return self.product_name[:10]


class Purchase(models.Model):
    bayer = models.ForeignKey(MyUser, on_delete=models.PROTECT, null=True, related_name='bayer')
    purchase = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='purchases')
    quantity = models.PositiveSmallIntegerField()
    time_of_purchase = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _("Purchase")
        verbose_name_plural = _("Purchases")
        ordering = ["-time_of_purchase"]

    def __str__(self):
        return f"Purchase #{self.pk}"

class Returns(models.Model):
    time_return = models.DateTimeField(default=timezone.now)
    returns = models.ForeignKey(Purchase, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Returns")
        verbose_name_plural = _("Returns")
        ordering = ["-time_return"]

    def __str__(self):
        return f"Return purchase #{self.returns.pk}"

