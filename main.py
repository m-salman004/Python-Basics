from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
Builder.load_string('''
<FirstScreen>:
    name : 'first'
    MDRoundFlatIconButton:
        icon: "language-python"
        icon_color:"white"
        md_bg_color: "blue"
        icon_size: "50sp"
        text: "Python Language"
        text_color: "white"
        line_color: "blue"
        font_size: "18sp"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:
            root.manager.current = 'Second'
    MDRoundFlatIconButton:
        text:"Dark Theme"
        md_bg_color: "blue"
        pos_hint:{'center_x':0.85,'center_y':0.1}
        text_color: "white"
        line_color: "blue"
        font_size: "18sp"   
        on_release:app.theme_dark()
    MDTextField:
        hint_text: "Enter Username"
        mode: "rectangle"
        pos_hint:{'center_x':.5,'center_y':.7}
        size_hint:{0.5,0.1}
        icon_right: "language-python"
        icon_right_color_normal: "blue"
        hint_text_color_normal: "blue"
        line_color_normal: "blue"
<SecondScreen>:
    name : 'second'
    MDRoundFlatIconButton:
        icon: "android"
        icon_color:"white"
        md_bg_color: "blue"
        icon_size: "50sp"
        text: "Android Development"
        text_color: "white"
        line_color: "blue"
        font_size: "18sp"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:
            root.manager.current = 'Third'
    MDRoundFlatIconButton:
        text:"Dark Theme"
        md_bg_color: "blue"
        pos_hint:{'center_x':0.85,'center_y':0.1}
        text_color: "white"
        line_color: "blue"
        font_size: "18sp"   
        on_release:app.theme_dark()
    MDTextField:
        hint_text: "Enter Email"
        mode: "rectangle"
        pos_hint:{'center_x':.5,'center_y':.7}
        size_hint:{0.4, None}
        icon_right: "android"
        icon_right_color_normal: "blue"
        hint_text_color_normal: "blue"
        line_color_normal: "blue"
        
<ThirdScreen>:
    name : 'third'
    MDRoundFlatIconButton:
        icon: "language-php"
        icon_color:"white"
        md_bg_color: "blue"
        icon_size: "50sp"
        text: "php Language"
        text_color: "white"
        line_color: "blue"
        font_size: "18sp"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:
            root.manager.current = 'four'
    MDRoundFlatIconButton:
        text:"Dark Theme"
        md_bg_color: "blue"
        pos_hint:{'center_x':0.85,'center_y':0.1}
        text_color: "white"
        line_color: "blue"
        font_size: "18sp"   
        on_release:app.theme_dark()

<FourthScreen>:
    name : 'four'
    MDRoundFlatIconButton:
        icon: "language-cpp"
        icon_color:"white"
        md_bg_color: "blue"
        icon_size: "50sp"
        text: "C++ Language"
        text_color: "white"
        line_color: "blue"
        font_size: "18sp"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:
            root.manager.current = 'fifth'
    MDRoundFlatIconButton:
        text:"Dark Theme"
        md_bg_color: "blue"
        pos_hint:{'center_x':0.85,'center_y':0.1}
        text_color: "white"
        line_color: "blue"
        font_size: "18sp"   
        on_release:app.theme_dark()

<FifthScreen>:
    name : 'fifth'
    MDRoundFlatIconButton:
        icon: "android"
        icon_color:"white"
        md_bg_color: "blue"
        icon_size: "50sp"
        text: "Mobile Application Development"
        text_color: "white"
        line_color: "blue"
        font_size: "18sp"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:
            root.manager.current = 'back'
    MDRoundFlatIconButton:
        text:"Dark Theme"
        md_bg_color: "blue"
        pos_hint:{'center_x':0.85,'center_y':0.1}
        text_color: "white"
        line_color: "blue"
        font_size: "18sp"   
        on_release:app.theme_dark()
    
<BackScreen>
    name:'back'
    MDRoundFlatIconButton:
        md_bg_color: "blue"
        text:'Back'
        text_color: "white"
        line_color: "blue"
        font_size: "28sp"
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

class FifthScreen(Screen):
    pass

class BackScreen(Screen):
    pass

class MultipleScreens(MDApp):
    def build(self):
        self.theme_cls.theme_style == "Light"
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='Second'))
        sm.add_widget(ThirdScreen(name='Third'))
        sm.add_widget(FourthScreen(name='four'))
        sm.add_widget(FifthScreen(name='fifth'))
        sm.add_widget(BackScreen(name='back'))
        return sm

    def theme_dark(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"

        else:
            self.theme_cls.theme_style = "Light"

obj = MultipleScreens()
obj.run()


# Class and Objects
# How to create a class
# class Username (self):
#     def __init__(self):
#
# print(Name)
