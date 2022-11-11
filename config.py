"""Configuration de l'application exercice Nevernote."""

DATABASE_FILE = "db.sqlite3"
MODEL_MODULES = [
    "nevernote.notes.models",
    "nevernote.tasks.models",
    "nevernote.users.models",
    "nevernote.tags.models",
]
