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
<SecondScreen>:
    name : 'second'   
     MDRectangleFlatIconButton:
        icon: "android"
        icon_color:"black"
        text: "Android Development"
        text_color: "black"
        line_color: "black"
        pos_hint:{'center_x':0.5,'center_y':0.5}

<ThirdScreen>:
    name : 'third'
    MDRectangleFlatIconButton:
        icon: "language-php"
        icon_color:"black"
        text: "php Language"
        text_color: "black"
        line_color: "black"
        pos_hint:{'center_x':0.5,'center_y':0.5}

<FourthScreen>:
    name : 'four'
    MDRectangleFlatIconButton:
        icon: "language-cpp"
        icon_color:"black"
        text: "C++ Language"
        text_color: "black"
        line_color: "black"
        pos_hint:{'center_x':0.5,'center_y':0.5}
''')