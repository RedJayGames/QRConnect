import os

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import qrcode


data = {}


class MainScreen(Screen):
    pass


class GenerateScreen(Screen):

    @staticmethod
    def checkbox_click(active, info_type, info_val):
        global data
        data[info_type] = {
            "active": active,
            "value": info_val
        }


class QRScreen(Screen):

    @staticmethod
    def generate_qr():

        img = qrcode.make(data)
        img.save('qr_code.png')
        return 'qr_code.png'


class ScanScreen(Screen):
    pass


class ContactScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("myApp.kv")


class MyApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run()
