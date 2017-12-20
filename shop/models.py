from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=250)
    category_desc = models.CharField(max_length=250)
    category_logo = models.FileField()

    # redirect
    def get_absolute_url(self):
        return reverse('gala:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.category_name


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=500)
    product_description = models.CharField(max_length=1000)
    product_count = models.CharField(max_length=250)
    product_price = models.CharField(max_length=250)

    # redirect
    def get_absolute_url(self):
        return reverse('gala:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.product_name + ', ' + self.product_description + ', ' + self.product_price
