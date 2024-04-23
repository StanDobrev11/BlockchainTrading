from django.db import models


# Create your models here.
class BaseCurrency(models.Model):
    """
    This class represents the currency symbol and name and will be abstract
    """

    class Meta:
        abstract = True

    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.symbol


class CryptoCurrency(BaseCurrency):
    is_crypto = models.BooleanField(default=True)


class FiatCurrency(BaseCurrency):
    is_fiat = models.BooleanField(default=True)


class CurrencyPair(models.Model):
    """
    The currency pair will be composed of crypto - fiat pairs
    """

    base_currency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE, related_name='base_currency_pairs')
    quote_currency = models.ForeignKey(FiatCurrency, on_delete=models.CASCADE, related_name='quote_currency_pairs')

    def __str__(self):
        return f"{self.base_currency}-{self.quote_currency}"
