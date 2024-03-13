from django.contrib.auth import models as auth_models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from BlockchainTrading.accounts.validators import min_date_of_birth_validator, max_date_of_birth_validator


# Create your models here

# inherit AbstractBaseUser to completely rewrite the user class including django admin
# here is where auth data is kept
class CustomUser(auth_models.AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': _('A user with that email already exists. Log in instead?')
        }

    )

    # using it as a primary log in credential together with the password
    # important to indicate usage of email as primary credential
    USERNAME_FIELD = 'email'

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)


# here is user data kept
class Profile(models.Model):
    user = models.OneToOneField(
        to=CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    date_of_birth = models.DateField(
        validators=[
            min_date_of_birth_validator,
            max_date_of_birth_validator,
        ],

        error_messages={
            'date_of_birth': _('Must be at least 18 years old with. Enter a valid date'),
        },
        blank=True,
        null=True,
    )
