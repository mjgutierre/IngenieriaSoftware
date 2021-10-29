#clase main del sistema de las vistas
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import Screen

from kivy.core.window import Window

Window.size=(260,500)
class MenuScreen(Screen):
    pass
class DriverScreen(Screen):
    pass
class RiderScreen(Screen):
    pass
class LogInScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class Default(Screen):
    pass
class RiderProfileScreen(Screen):
    pass
class WindowManager(ScreenManager):
    pass
kiv=Builder.load_file(("main.kv"))

class Pricar(MDApp):
    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette="Blue"



        return kiv
    def login(self):
        pass
Pricar().run()
