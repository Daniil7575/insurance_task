from datetime import datetime

from tortoise import fields
from tortoise.models import Model


class Date(Model):
    date = fields.DateField(pk=True, default=datetime.now)


class CargoType(Model):
    date = fields.ForeignKeyField("models.Date", "cargos")
    cargo_type = fields.CharField(50, null=False)
    rate = fields.DecimalField(6, 4)
