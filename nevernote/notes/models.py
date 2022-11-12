from nevernote.core import models
from nevernote.core.database import register_model
from nevernote.tags.models import Tag


@register_model
class Note(models.Model):
    """Représente une note dans le carnet."""

    title = models.CharField(max_length=255)
    content = models.TextField(null=True)


@register_model
class NoteTag(models.Model):
    """Représente l'association entre une étiquette et une note."""

    note = models.ForeignKeyField(Note, backref="tags")
    tag = models.ForeignKeyField(Tag, backref="notes")


@register_model
class Notebook(models.Model):
    """Représente un carnet de notes."""

    name = models.CharField(max_length=255)
