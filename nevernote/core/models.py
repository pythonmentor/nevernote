from datetime import datetime

from peewee import (
    AutoField,
    BigIntegerField,
    CharField,
    DateField,
    DateTimeField,
    TimeField,
    FloatField,
    DoubleField,
    DecimalField,
    IntegerField,
    TextField,
    ForeignKeyField,
    BooleanField,
)
from peewee import Model as BaseModel

from nevernote.utils import timezone_now
from nevernote.core.database import database


class Model(BaseModel):
    """Base pour tous les modèles de l'application."""

    created = DateTimeField(default=timezone_now)
    updated = DateTimeField(default=timezone_now)

    class Meta:
        database = database

    def save(self, *args, **kwargs):
        """Sauve le modèle en modifiant la date de mise à jour."""
        self.updated = timezone_now()
        return super().save(*args, **kwargs)
