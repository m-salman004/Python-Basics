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
            padding: dp(4), dp(25)
            spacing: dp(4)
            MDLabel:
                text: "Hello World " 
            MDLabel:
                text: "Hello World"
            MDLabel:
                text: "Hello World"
            MDLabel:
                text: "Hello World"
           
    
'''

