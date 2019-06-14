from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
import random
Window.size = (570, 400)

class Frame(Widget):
    no = 0
    n = 0
    def calculate(self, *args):
        Clock.unschedule(self.update)
        f = self.ids['first']
        s = self.ids['second']
        e = self.ids['error']
        p = self.ids['per']
        e.text = ''
        e.color = (0, 0, 0, 1)
        p.text = ''
        if f.text == '' or s.text == '':
            e.text = 'Type a names in both fields'#
        else:
            self.n = 0
            Clock.schedule_interval(self.update, 1/3)

    def update(self, *args):
        e = self.ids['error']
        self.n += 0.333
        ti = random.randrange(1, 4)
        if self.n >= ti:
            self.display()
            Clock.unschedule(self.update)
        else:
            if self.no >= 3:
                self.base = -1
            if self.no == 0:
                self.base = 1
            self.no += self.base
            e.text = 'Loading{}'.format('.'*self.no)

    def display(self, *args):
        e = self.ids['error']
        p = self.ids['per']
        x = random.randrange(1, 101)
        if x == 100:
            e.text = 'Perfect!'
            e.color = (0, 1, 0, 1)
            p.text = '{}%'.format(str(x))
            p.color = (0, 1, 0, 1)
        elif x > 75:
            e.text = "Very Compatible!"
            e.color = (0, 1, 1, 1)
            p.text = '{}%'.format(str(x))
            p.color = (0, 1, 1, 1)
        elif x > 50:
            e.text = "Slighty Compatible!"
            e.color = (0, 0.85, 0.9, 1)
            p.text = '{}%'.format(str(x))
            p.color = (0, 0.85, 0.9, 1)
        elif x > 33:
            e.text = "Not So Compatible!"
            e.color = (0, 0, 1, 1)
            p.text = '{}%'.format(str(x))
            p.color = (0, 0, 1, 1)
        else:
            e.text = "Incompatible!"
            e.color = (1, 0, 0, 1)
            p.text = '{}%'.format(str(x))
            p.color = (1, 0, 0, 1)

Builder.load_file('love calculator.kv')

class Main(App):
    def build(self):
        return Frame()

Main().run()
