from nevernote.core.controllers import (
    AbstractMenuController,
)
from nevernote.core.menus import Menu
from nevernote.core.views import SimpleCursesMenuView


class HomeController(AbstractMenuController):
    """Contrôle le menu d'accueil de l'application."""

    def get_menu(self):
        """Défini le menu d'accueil"""
        from nevernote.menus.notebooks.controllers import NotebookController

        return (
            Menu("Accueil")
            .add("Carnets de notes", NotebookController(self.application))
            .add("Toutes les notes")
            .add("Etiquettes")
            .add("Tâches")
            .add("Quitter l'application")
        )


class ExempleFullyManualHomeController:
    """Contrôle le menu d'accueil de l'application.

    Implémentation à la main."""

    def __init__(self, application):
        self.application = application
        self.state = application.state

    def __call__(self):
        """Exécution du contrôleur."""
        menu = (
            Menu("Accueil")
            .add("Carnets de notes")
            .add("Toutes les notes")
            .add("Etiquettes")
            .add("Tâches")
            .add("Quitter l'application")
        )

        home_view = SimpleCursesMenuView(self.application, menu)
        home_view.render()
        user_choice = home_view.get_user_choice()

        if user_choice in menu:
            return menu.get(user_choice)
        else:
            return self
