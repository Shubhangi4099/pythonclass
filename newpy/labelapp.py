import  kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
class SpartaGrid(GridLayout):
    def __init__(self,**kwargs):
        super(SpartaGrid, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='student name'))
        self.s_name=TextInput()
        self.add_widget(self.s_name)

        class SpartaApp(App)
            def build(self):
                return SpartaGrid()
            if __name__ =="__labelapp__":
                SpartaApp().run()


