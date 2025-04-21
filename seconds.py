# напиши модуль для реализации секундомера
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty, NumericProperty, StringProperty

class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        self.done = False
        self.timer_text = 'Секунд прошло:' + str(self.current)
        super().__init__(text=self.timer_text)

    def start(self):
        Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.current += 1
        self.text = 'Секунд прошло:' + str(self.current)
        if self.current >= self.total:
            self.done = True
            return False

    def restart(self, total, **kwargs):
        self.current = 0
        self.total= total
        self.done = False
        self.timer_text = 'Секунд прошло:' + str(self.current)
        self.start()
