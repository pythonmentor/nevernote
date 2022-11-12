import abc


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

    @property
    @abc.abstractclassmethod
    def menu(self):
        """Menu utilisé pour gérer la saisie utilisateur."""

    @property
    @abc.abstractclassmethod
    def view_class(self):
        """Vue utilisée pour gérer l'affichage du menu et la saisie utilisateur."""

    def __call__(self):
        """Exécution générique pour un contrôler de menu."""
        view = self.view_class(self.application, self.menu)
        user_choice = view.render()
        if user_choice in self.menu:
            return self.menu.get(user_choice)
        else:
            return self
