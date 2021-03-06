from django.db import models
from django.core.exceptions import ValidationError
import datetime


# Create your models here.
class SleepRecord(models.Model):
    def validate_max(value):
        if value > 5:
            raise ValidationError(
                _('%(value)s is bigger than 5'),
                params={'value': value},
            )

    def validate_day(value):
        if value > 23:
            raise ValidationError(
                _('%(value)s is bigger than 23'),
                params={'value': value},
            )
        elif value < 0:
            raise ValidationError(
                _('%(value)s is smaller than 0'),
                params={'value': value},
            )

    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('auth.user',
                              related_name='sleep_owner',
                              on_delete=models.CASCADE,
                              null=False)
    date = models.DateField(auto_now_add=True)
    sleep_at = models.IntegerField(default=-1, validators=[validate_max])
    hours = models.FloatField(null=False, default=-1)
    satisfaction_score = models.PositiveIntegerField(validators=[validate_max],
                                                     null=False)
    tiredness = models.PositiveIntegerField(validators=[validate_max],
                                            null=False)
