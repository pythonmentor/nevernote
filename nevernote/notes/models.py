from nevernote.core import models
from nevernote.core.database import register_model


@register_model
class Notebook(models.Model):
    ...


@register_model
class Note(models.Model):
    ...
