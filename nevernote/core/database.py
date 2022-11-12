from importlib import import_module

from peewee import SqliteDatabase

import config

_registered_models = []

database = SqliteDatabase(config.DATABASE_FILE)


def register_model(model):
    """Décorateur pour enregistrer les modèles de l'application."""
    _registered_models.append(model)
    return model


def load_models():
    """Charge les modèles enregistré de l'application."""
    for model in config.MODEL_MODULES:
        import_module(model)


def create_tables():
    """Crée les tables en base de données."""
    database.create_tables(_registered_models)
