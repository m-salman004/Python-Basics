from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
Builder_string = '''
ScreenManager:
    First:
<First>:
    name:"first"
    MDLabel:
        id: A
        text: "Hello World"
    
'''