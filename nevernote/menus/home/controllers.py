from nevernote.core.controllers import (
    AbstractController,
    AbstractMenuController,
)
from nevernote.core.menus import Menu

from .views import HomeView


class HomeController(AbstractMenuController):
    """Contrôle le menu d'accueil.

    Implémentation utilisant un MenuController générique."""

    menu = (
        Menu("Accueil")
        .add("Carnets de notes", None)
        .add("Toutes les notes", None)
        .add("Etiquettes", None)
        .add("Tâches", None)
        .add("Quitter l'application", None)
    )

    view_class = HomeView


class FullHomeController(AbstractController):
    """Contrôle le menu d'accueil de l'application.

    Implémentation utilisant un Controller générique de base."""

    def __call__(self):
        """Exécution du contrôleur."""
        menu = (
            Menu("Accueil")
            .add("Carnets de notes", None)
            .add("Toutes les notes", None)
            .add("Etiquettes", None)
            .add("Tâches", None)
            .add("Quitter l'application", None)
        )

        home_view = HomeView(self.application, menu)
        user_choice = home_view.render()

        if user_choice in menu:
            return menu.get(user_choice)
        else:
            return self
