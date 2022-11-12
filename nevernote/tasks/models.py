from nevernote.core import models
from nevernote.tags.models import Tag
from nevernote.core.database import register_model


@register_model
class Task(models.Model):
    """Représente une tâche associée à une note."""

    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    due_datetime = models.DateTimeField(null=True)
    recurring = models.BooleanField(default=False)
    done = models.BooleanField(default=False)


@register_model
class TagTask(models.Model):
    """Représente l'association entre une étiquette et une tâche."""

    task = models.ForeignKeyField(Task, backref="tags")
    tag = models.ForeignKeyField(Tag, backref="tasks")
