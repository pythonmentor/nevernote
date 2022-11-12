"""Configuration de l'application exercice Nevernote."""
import locale

TERMINAL_ENCODING = locale.getdefaultlocale()[1]
DATABASE_FILE = "db.sqlite3"
MODEL_MODULES = [
    "nevernote.notes.models",
    "nevernote.tasks.models",
    "nevernote.tags.models",
]
TIME_ZONE = "Europe/Paris"

DEFAULT_NOTEBOOK_NAME = "Boîte de réception"
DEFAULT_NOTE_FOR_TASKS = "Choses à faire"
