from nevernote.core.controllers import AbstractMenuController
from nevernote.core.menus import Menu


class NotebookController(AbstractMenuController):
    def get_menu(self):
        from nevernote.menus.home.controllers import HomeController

        return (
            Menu("Gestion des carnets de note")
            .add("Consulter les carnets de notes disponibles")
            .add("Créer un nouveau carnet de notes")
            .add(
                "Revenir à l'accueil",
                HomeController(self.application),
            )
            .add("Quitter l'application")
        )
