import abc
import curses

from . import template_environment


class SimpleCursesMenuView(abc.ABC):
    """Vue de base pour l'affichage des menu"""

    def __init__(
        self,
        application,
        menu,
        menu_template="menu.txt",
        template_environment=template_environment,
    ):
        """Crée une vue gérant un menu simple à l'aide de curses."""
        self.window = application.window
        self.menu = menu
        self.menu_template = menu_template
        self.template_environment = template_environment

    def render_menu(self):
        """Crée la représentation textuelle du menu."""
        template = self.template_environment.get_template(self.menu_template)
        return template.render(menu=self.menu)

    def get_user_choice(self):
        """Demande à l'utilisateur de faire un choix parmi les options."""
        return self.window.getkey()

    def render(self):
        """Gère l'affichage du menu à l'écran."""
        curses.curs_set(False)
        self.window.clear()
        self.window.addstr(self.render_menu())
        self.window.refresh()
