from nevernote.core import models
from nevernote.core.database import register_model


@register_model
class Tag(models.Model):
    """Représente une étiquette à associer à une note ou à une tâche."""

    name = models.CharField(max_length=100)
