from datetime import datetime, date, timedelta

from django.core.exceptions import ValidationError


def min_date_of_birth_validator(value):
    if value < date(1900, 1, 1):
        raise ValidationError('Year must be greater than or equal to 1900')


def max_date_of_birth_validator(value: datetime):
    if int(datetime.now().strftime('%Y')) - int(value.strftime('%Y')) >= 18:
        if int(datetime.now().strftime('%m')) >= int(value.strftime('%m')):
            if int(datetime.now().strftime('%d')) >= int(value.strftime('%d')):
                return
    raise ValidationError('User must be at least 18 years old')
