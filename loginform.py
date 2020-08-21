from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""

<Login>:
    GridLayout:
        cols:2
        
        TextInput: 
            id: username

        TextInput:
            id: pass
        
        Button:
            text: 'Enter'
            on_press: 
                if username.text == "test" and pass.text == "123":
                    root.manager.current = SettingsScreen


        Button:
            text: 'Quit'


<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'login'
""")

# Declare both screens
class Login(Screen):
    pass

class SettingsScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(Login(name='login'))
sm.add_widget(SettingsScreen(name='settings'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()