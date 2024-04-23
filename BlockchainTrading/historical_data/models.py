from django.db import models


class HistoricalData(models.Model):
    date = models.DateField()
    open = models.DecimalField(max_digits=19, decimal_places=10)
    high = models.DecimalField(max_digits=19, decimal_places=10)
    low = models.DecimalField(max_digits=19, decimal_places=10)
    close = models.DecimalField(max_digits=19, decimal_places=10)
    volume = models.DecimalField(max_digits=19, decimal_places=10)

    class Meta:
        abstract = True
