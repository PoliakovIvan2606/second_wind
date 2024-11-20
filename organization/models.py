from django.db import models
from django.core.exceptions import ValidationError

def validate_numeric_string(value):
    if len(value) != 18:
        raise ValidationError('Должно быть ровно 18 символов.')
    if not value.isdigit():
        raise ValidationError('Строка должна содержать только цифры.')

class Organization(models.Model):
    ogrn = models.CharField(max_length=18, validators=[validate_numeric_string])

    def clean(self):
        if len(self.ogrn) != 18:
            raise ValidationError("OGRN должен быть длиной 13 символов.")
        elif not self.ogrn.isdigit():
            raise ValidationError("OGRN должен содержать только цифры.")

    def save(self, *args, **kwargs):
        # Вызываем clean перед сохранением
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ogrn
