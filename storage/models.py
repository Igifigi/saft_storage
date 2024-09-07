from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils import timezone

# Create your models here.

def validate_ean13(value):
    if len(str(value)) != 13:
        raise ValidationError(_('Barcode must be 13 digits.'))

def validate_phone_number(value):
    if len(str(value)) != 9:
        raise ValidationError(_('Phone number must be 9 digits.'))

class ToolTag(models.Model):
    name = models.CharField(max_length=25)

class Tool(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    barcode = models.IntegerField(validators=[validate_ean13]) # in EAN13 format; TODO: generate barcode with new record in the db
    tags = models.ManyToManyField(ToolTag, blank=True)

class LenderTeam(models.Model):
    name = models.CharField(max_length=25)

class Lender(models.Model):
    name = models.CharField(max_length=40)
    phone = models.IntegerField(validators=[validate_phone_number])
    team = models.ForeignKey(LenderTeam, on_delete=models.DO_NOTHING, blank=True)
    blacklisted = models.BooleanField(default=False)

class Rental(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
