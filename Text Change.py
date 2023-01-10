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
        font_size: "20sp"
        pos_hint:{'center_x':0.92,'center_y':0.5}
    MDRectangleFlatButton:
        text: "Change Text"
        md_bg_color: "blue"
        text_color: "white"
        line_color: "blue"
        font_size: "20sp"
        pos_hint:{'center_x':0.5,'center_y':0.10}
        
'''

class First(Screen):
    pass

sm = ScreenManager()
sm.add_widget(First(name='first'))

class Textchange(MDApp):
    def change_text(self):
       self.string.get_screen('first').ids.A.text = "Text Changing "

    def build(self):
        self.string = Builder.load_string(Builder_string)
        return self.string
    
Textchange().run()