from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
Builder.load_string('''
<FirstScreen>:
    name : 'first'
    MDRectangleFlatIconButton:
        icon: "language-python"
        icon_color:"black"
    


''')