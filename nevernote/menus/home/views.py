import curses

from .. import template_environment


class HomeView:
    def __init__(self, application, menu):
        self.window = application.window
        self.menu = menu

    def render_menu(self):
        template = template_environment.get_template("menu.txt")
        return template.render(menu=self.menu)

    def render(self):
        curses.curs_set(False)
        self.window.clear()
        self.window.addstr(self.render_menu())
        self.window.refresh()
        return self.window.getkey()
