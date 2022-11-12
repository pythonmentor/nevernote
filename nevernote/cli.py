import curses

from nevernote.core.controllers import Application
from nevernote.menus.home.controllers import HomeController


def application(window):
    """Démarre l'application."""
    app = Application(window=window, controller=HomeController)
    app.start()


def main():
    """Point d'entrée principal de l'application en ligne de commande."""
    curses.wrapper(application)
