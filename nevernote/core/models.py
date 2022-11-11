from peewee import (
    AutoField,
    BigIntegerField,
    CharField,
    DateField,
    DateTimeField,
    FloatField,
    IntegerField,
)
from peewee import Model as BaseModel
from peewee import TextField

from .database import database


class Model(BaseModel):
    """Base pour tous les modèles de l'application."""

    class Meta:
        database = database
