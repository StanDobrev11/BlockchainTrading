from django.contrib import admin

from BlockchainTrading.currency.models import CryptoCurrency, FiatCurrency, CurrencyPair


# Register your models here.
@admin.register(CryptoCurrency)
class CryptoCurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(FiatCurrency)
class FiatCurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(CurrencyPair)
class CurrencyPairAdmin(admin.ModelAdmin):
    pass
