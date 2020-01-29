# =========
# =========
# IMPORTS
# =========
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.config import Config

# =========
# CLASS
# =========
class Calculator(Widget):
    onDisplay = ''
    operation = ''

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)

    def control(self, value):
        if value == 'C':
            self.operation = ''
            self.onDisplay = ''
            self.change_text(self.onDisplay)
        elif value == 'DEL':
            self.onDisplay = self.onDisplay[:-1]
            self.operation = self.operation[:-1]
            self.change_text(self.onDisplay)
        elif value == 'x':
            self.onDisplay += 'x'
            self.operation += '*'
            self.change_text(self.onDisplay)
        elif value == '=':
            try:
                result = str(eval(self.operation))
                self.change_text(result)
                self.onDisplay = result
                self.operation = result
            except Exception as e:
                #print(e)
                self.onDisplay = ''
                self.operation = ''
                self.change_text(self.onDisplay)
        else:
            self.onDisplay += str(value)
            self.operation += str(value)
            self.change_text(self.onDisplay)

    def change_text(self, text):
        if type(text) == float:
            self.display.text = str(round(text, 4))
        else:
            self.display.text = str(text)

class MainWindow(App):
    title = 'Számológép'
    icon = 'view/icon.png'
    def build(self):
        return Calculator()


# =========
# MAINS
# =========
Builder.load_file('view/view.kv')
Config.set('input', 'mouse', 'mouse, multitouch_on_demand')

if __name__ == '__main__':
    MainWindow().run()
