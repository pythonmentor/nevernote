import abc

from .views import SimpleCursesMenuView


class Application:
    """Contrôleur frontal de l'application."""

    def __init__(self, window, controller):
        self.window = window
        self.state = {}
        self.next_controller = controller(application=self)

    def start(self):
        """Démarre l'application."""
        while self.next_controller:
            self.next_controller = self.next_controller()


class AbstractController(abc.ABC):
    """Base pour tout les contrôleurs."""

    def __init__(self, application):
        self.application = application
        self.state = application.state

    @abc.abstractmethod
    def __call__(self):
        """Exécute les actions du contrôleur."""


class AbstractMenuController(AbstractController):
    """Contrôleur abstrait servant de base pour tous les menus de l'application."""

    view_class = SimpleCursesMenuView

    @abc.abstractclassmethod
    def get_menu(self):
        """Menu utilisé pour gérer la saisie utilisateur."""

    def get_view(self, menu):
        """Construit l'objet responsable de créer la vue."""
        return self.view_class(self.application, menu)

    def __call__(self):
        """Exécution générique pour un contrôler de menu."""
        menu = self.get_menu()
        view = self.get_view(menu)
        view.render()
        user_choice = view.get_user_choice()

        if user_choice in menu:
            return menu[user_choice]
        else:
            return self
