from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class Catalog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг", validators=[
        MinLengthValidator(5, message="Минимум 5 символов"),
        MaxLengthValidator(100, message="Максимум 100 символов"),
    ])
    parent = models.ForeignKey('Catalog', on_delete=models.CASCADE, null=True, related_name='children')

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    comments_counter = models.PositiveIntegerField()
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг", validators=[
        MinLengthValidator(5, message="Минимум 5 символов"),
        MaxLengthValidator(100, message="Максимум 100 символов"),
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    catalog = models.ManyToManyField(Catalog)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None,
                              blank=True, null=True, verbose_name="Фото")
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=None)
    is_bestseller = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)


class ProductPhoto(models.Model):
    url = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductSet(models.Model):
    property_set = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Property(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
