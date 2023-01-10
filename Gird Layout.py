from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
Builder_string = '''
ScreenManager:
    First:
<First>:
    name:"first"
    ScrollView:
        MDGridLayout:
            adaptive_height: True
            cols:4
