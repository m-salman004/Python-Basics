from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
Builder.load_string('''
<FirstScreen>:
    name : 'first'
    MDRectangleFlatIconButton:
        icon: "language-python"
        icon_color:"black"
        text: "Python Language"
        text_color: "black"
        line_color: "black"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:
            root.manager.current = 'Second'
<SecondScreen>:
    name : 'second'   
    MDRectangleFlatIconButton:
        icon: "android"
        icon_color:"black"
        text: "Android Development"
        text_color: "black"
        line_color: "black"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:
            root.manager.current = 'Third'

<ThirdScreen>:
    name : 'third'
    MDRectangleFlatIconButton:
        icon: "language-php"
        icon_color:"black"
        text: "php Language"
        text_color: "black"
        line_color: "black"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:
            root.manager.current = 'four'

<FourthScreen>:
    name : 'four'
    MDRectangleFlatIconButton:
        icon: "language-cpp"
        icon_color:"black"
        text: "C++ Language"
        text_color: "black"
        line_color: "black"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:
            root.manager.current = 'back'
        
<BackScreen>
    name:'back'
    MDRectangleFlatIconButton:
        text:'Back'
        text_color:"black"
        line_color:"black"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:
            root.manager.current = 'first'
''')

class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

class FourthScreen(Screen):
    pass

class BackScreen(Screen):
    pass

class MultipleScreens(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='Second'))
        sm.add_widget(ThirdScreen(name='Third'))
        sm.add_widget(FourthScreen(name='four'))
        sm.add_widget(BackScreen(name='back'))
        return sm


obj = MultipleScreens()
obj.run()