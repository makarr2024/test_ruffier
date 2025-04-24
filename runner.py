# напиши модуль для работы с анимацией
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, NumericProperty, StringProperty
from kivy.animation import Animation
from kivy.uix.button import Button

class Runner(BoxLayout):
    value = NumericProperty(0)
    finished = BooleanProperty(False)
    def __init__(self, total, steptime):
        self.total = total
        self.animation = (Animation(pos_hint={'top': 0.1}, duration=steptime/2) + Animation(pos_hint={'top': 1.0}, duration=steptime/2))
        btn = Button(text='-------------')
        btn.add_widget(BoxLayout)
        self.animation.on_progress(self.next)

    def start(self):
        self.value = 0
        self.finished = False
        self.animation.repeat = True
        self.animation.start(self.btn)



    def next(self, widget, step):
        if step == 1.0:
            step += 1
            if self.value > self.total:
                self.animation.repeat = False
                self.finished = True
