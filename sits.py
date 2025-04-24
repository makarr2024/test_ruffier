# напиши модуль для подсчета количества приседаний
from kivy.uix.label import Label

class Sits(Label):
    
    def __init__(self, total, **kwargs):
        self.sits_now = 0
        self.total = total
        sits_rem_txt = 'Осталось приседаний:' + str(total)
        super().__init__(text=sits_rem_txt, **kwargs)

    def next(self, *args):
        self.current += 1
        remain = max(0, self.total - self.current)
        self.text = 'Осталось приседаний:' + str(remain)
