from django.db import models
from django.core.exceptions import ValidationError

def validate_numeric_string(value):
    if len(value) != 18:
        raise ValidationError('Должно быть ровно 18 символов.')
    if not value.isdigit():
        raise ValidationError('Строка должна содержать только цифры.')

class Organization(models.Model):
    ogrn = models.CharField(max_length=18, validators=[validate_numeric_string])

    def __str__(self):
        return self.ogrn
