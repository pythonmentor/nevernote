import config
from nevernote.core.database import create_tables, load_models
from nevernote.notes.models import Note, Notebook

# Charge les modèles et initilise la base de données
load_models()
create_tables()

# Création de la note et du carnet de note par défaut
Note.get_or_create(title=config.DEFAULT_NOTE_FOR_TASKS)
Notebook.get_or_create(name=config.DEFAULT_NOTEBOOK_NAME)
