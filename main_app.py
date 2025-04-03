from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from ruffier import test

class MyButton(Button):
    def __init__(self, screen, direction, goal, **kwargs):
        super().__init__(**kwargs)
        self.goal = goal
        self.screen = screen
        self.direction = direction
    
    def on_press(self):
        self.screen.manager.transition.drection = self.direction
        self.screen.manager.current = self.goal




class FirstScr(Screen):
    def __init__(self, name='first',**kwargs):
        super().__init__(name=name,**kwargs)

# widgets
        ti_text1 = Label(text = 'Введите имя')
        ti_text2 = Label(text = 'Введите возраст')
        self.ti_name = TextInput()
        self.ti_age = TextInput()
        btn = Button(text="Продолжить", size_hint=(.5, .3), pos_hint={'center_x': 1})
        btn.on_press = self.next
        txt_instruction = Label(pos_hint={'center_y': .7},text = '''
Данное приложение позволит вам с помощью теста Руфье \n провести первичную диагностику вашего здоровья.\n
Проба Руфье представляет собой нагрузочный комплекс, \n предназначенный для оценки работоспособности сердца при физической нагрузке.\n
У испытуемого определяют частоту пульса за 15 секунд.\n
Затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n
После окончания нагрузки пульс подсчитывается вновь: \nчисло пульсаций за первые 15 секунд, 30 секунд отдыха,\n число пульсаций за последние 15 секунд.\n''')
        
# layouts 
        layout1 = BoxLayout(orientation='vertical', padding=8, spacing=8)
        layout2 = BoxLayout(orientation='horizontal', pos_hint={'center_x': .4, 'center_y': .2}, size_hint = (.7, .08))
        layout3 = BoxLayout(orientation='horizontal', pos_hint={'center_x': .4, 'center_y': .2}, size_hint = (.7, .08))
        layout4 = BoxLayout(orientation='horizontal', size_hint=(.2, .3), pos_hint={'center_x': .5})
# add widgets
        layout1.add_widget(txt_instruction)
        layout2.add_widget(ti_text1)
        layout2.add_widget(self.ti_name)
        layout3.add_widget(ti_text2)
        layout3.add_widget(self.ti_age)
        layout4.add_widget(btn)
# add layouts
        layout1.add_widget(layout2)
        layout1.add_widget(layout3)
        layout1.add_widget(layout4)
# add on 1scr
        self.add_widget(layout1)
        
    def next(self):
        global name
        global age
        name = self.ti_name.text
        age = int(self.ti_age.text)

        self.manager.transition.direction = 'left'
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second',**kwargs):
        super().__init__(name=name,**kwargs)
        txt_test1 = Label(text = 'Замерьте пульс за 15 секунд.\nРезультат запишите в соответствующее поле.')
        
        btn = Button(text="Продолжить", size_hint=(.6, .4), pos_hint={'center_x': 1})
        ti_text1 = Label(text = 'Введите результат')
        self.ti_res1 = TextInput()
        btn.on_press = self.next
        layout1 = BoxLayout(orientation = 'vertical', size_hint = (1, .6), padding=8, spacing=8)
        layout2 = BoxLayout(orientation='horizontal', size_hint=(.5, .15), pos_hint={'center_x': .465})
        layout3 = BoxLayout(orientation='horizontal', size_hint=(.2, .4), pos_hint={'center_x': .5})

        layout1.add_widget(txt_test1)
        layout2.add_widget(ti_text1)
        layout2.add_widget(self.ti_res1)
        layout3.add_widget(btn)
        layout1.add_widget(layout2)
        layout1.add_widget(layout3)
        self.add_widget(layout1)
        
    def next(self):
        global res1
        res1 = int(self.ti_res1.text)
        self.manager.transition.direction = 'left'
        self.manager.current = 'third'

class ThirdScr(Screen):
    def __init__(self, name='third',**kwargs):
        super().__init__(name=name,**kwargs)
        txt_sits = Label(text ='Выполните 30 приседаний за 45 секунд.')
        btn = Button(text="Продолжить")
        btn.on_press = self.next

        layout = BoxLayout(orientation = 'vertical')
        layout1 = BoxLayout(orientation = 'horizontal', pos_hint={'center_x': .5, 'center_y': .3}, size_hint=(.2, .1), padding=8, spacing=8)
        layout.add_widget(txt_sits)
        layout1.add_widget(btn)
        layout.add_widget(layout1)
        
        self.add_widget(layout)
        

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'fourth'

class FourthScr(Screen):
    def __init__(self, name='fourth',**kwargs):
        super().__init__(name=name,**kwargs)
# widgets
        ti_text1 = Label(text = 'Результат',)
        ti_text2 = Label(text = 'Результат после отдыха')

        self.ti_res2 = TextInput()
        self.ti_res3 = TextInput()
        btn = Button(text="Завершить", size_hint=(.5, .3), pos_hint={'center_x': 1})
        btn.on_press = self.next
        txt_test3 = Label(text='''В течение минуты замерьте пульс два раза:\n 
за первые 15 секунд минуты, затем за последние 15 секунд.\n
Результаты запишите в соответствующие поля.''')
# layouts 
        layout1 = BoxLayout(orientation='vertical', padding=8, spacing=8)
        layout2 = BoxLayout(orientation='horizontal', pos_hint={'center_x': .4, 'center_y': .2}, size_hint = (.7, .08))
        layout3 = BoxLayout(orientation='horizontal', pos_hint={'center_x': .4, 'center_y': .2}, size_hint = (.7, .08))
        layout4 = BoxLayout(orientation='horizontal', size_hint=(.2, .3), pos_hint={'center_x': .5})
# add widgets
        layout1.add_widget(txt_test3)
        layout2.add_widget(ti_text1)
        layout2.add_widget(self.ti_res2)
        layout3.add_widget(ti_text2)
        layout3.add_widget(self.ti_res3)
        layout4.add_widget(btn)
# add layouts
        layout1.add_widget(layout2)
        layout1.add_widget(layout3)
        layout1.add_widget(layout4)
# add on 1scr
        self.add_widget(layout1)
        
    def next(self):
        global res2
        global res3
        res2 = int(self.ti_res2.text)
        res3 = int(self.ti_res3.text)
        self.manager.transition.direction = 'left'
        self.manager.current = 'fifth'
        print(name, age, res1, res2, res3)

        

class FifthScr(Screen):
    def __init__(self, name='fifth',**kwargs):
        super().__init__(name=name,**kwargs)
        self.instr = Label(text='')
        self.on_enter = self.before
        self.add_widget(self.instr)

    def before(self):
        global res1
        global res2
        global res3
        global age
        self.instr.text = test(res1, res2, res3, age)
    
        


class MyApp(App):
        def build(self):
            sm = ScreenManager()
            sm.add_widget(FirstScr())
            sm.add_widget(SecondScr())
            sm.add_widget(ThirdScr())
            sm.add_widget(FourthScr())
            sm.add_widget(FifthScr())
            return sm


app = MyApp()
app.run()
