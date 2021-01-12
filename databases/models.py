from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    product_name = models.CharField(_("product name"), max_length=100)
    manufacturer = models.CharField(_('manufacturer'), max_length=100)
    date_of_manufacture = models.DateField(_("date of manufacture"), null=True, blank=True)


class City(models.Model):
    name = models.CharField(_('name'), max_length=100)


class Client(models.Model):
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)
    product = models.ManyToManyField(Product, verbose_name=_("product"),
                                     help_text=_("Select a product for this client"))
    city = models.ForeignKey("City", verbose_name=_("city"), on_delete=models.SET_NULL, null=True)


class Provider(models.Model):
    city = models.OneToOneField('City', on_delete=models.CASCADE)
    provider_name = models.TextField(_("provider name"), max_length=10, help_text=_("Provider_name"))
