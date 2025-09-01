from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout as fl
from kivy.uix.button import Button as b
from kivy.uix.label import Label as l
from kivy.uix.widget import Widget as w
import pygame


class MyApp(App):
    def __init__(self,**kwrags):   
        super().__init__(**kwrags)
        self.title="Calculator"
        self.icon="calc.png"
    def build(self):
        return MainF()

class MainF(fl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        output= l(text="...", font_size=30, size_hint=(.6, .2), pos_hint={'center_x': .5, 'center_y': .95})
        self.b1 = b(text="1", size_hint=(.3, .2), pos_hint={'center_x': .15, 'center_y': .7})
        self.b2 = b(text="2", size_hint=(.3, .2), pos_hint={'center_x': .45, 'center_y': .7})
        self.b3 = b(text="3", size_hint=(.3, .2), pos_hint={'center_x': .75, 'center_y': .7})
        self.b4 = b(text="4", size_hint=(.3, .2), pos_hint={'center_x': .15, 'center_y': .5})
        self.b5 = b(text="5", size_hint=(.3, .2), pos_hint={'center_x': .45, 'center_y': .5})
        self.b6 = b(text="6", size_hint=(.3, .2), pos_hint={'center_x': .75, 'center_y': .5})
        self.b7 = b(text="7", size_hint=(.3, .2), pos_hint={'center_x': .15, 'center_y': .3})
        self.b8 = b(text="8", size_hint=(.3, .2), pos_hint={'center_x': .45, 'center_y': .3})
        self.b9 = b(text="9", size_hint=(.3, .2), pos_hint={'center_x': .75, 'center_y': .3})
        self.b0 = b(text="0", size_hint=(.3, .2), pos_hint={'center_x': .45, 'center_y': .1})
        self.bclr = b(text="AC", size_hint=(.3, .2), pos_hint={'center_x': .15, 'center_y': .1})
        self.bback = b(text="<-", size_hint=(.3, .2), pos_hint={'center_x': .75, 'center_y': .1})
        self.badd = b(text="+", size_hint=(.1, .16), pos_hint={'center_x': .95, 'center_y': .72})
        self.bsub = b(text="-", size_hint=(.1, .16), pos_hint={'center_x': .95, 'center_y': .56})
        self.bmul = b(text="*", size_hint=(.1, .16), pos_hint={'center_x': .95, 'center_y': .40})
        self.bdiv = b(text="/", size_hint=(.1, .16), pos_hint={'center_x': .95, 'center_y': .24})
        self.beq = b(text="=", size_hint=(.1, .16), pos_hint={'center_x': .95, 'center_y': .08})
        self.brb = b(text=")", size_hint=(.1, .05), pos_hint={'center_x': .05, 'center_y': .875})
        self.lrb = b(text="(", size_hint=(.1, .05), pos_hint={'center_x': .05, 'center_y': .825})        

        self.brb.bind(on_press=lambda instance: self.on_operator_press(')'))
        self.lrb.bind(on_press=lambda instance: self.on_operator_press('('))
        self.b1.bind(on_press=lambda instance: self.on_number_press('1'))
        self.b2.bind(on_press=lambda instance: self.on_number_press('2'))
        self.b3.bind(on_press=lambda instance: self.on_number_press('3'))
        self.b4.bind(on_press=lambda instance: self.on_number_press('4'))
        self.b5.bind(on_press=lambda instance: self.on_number_press('5'))
        self.b6.bind(on_press=lambda instance: self.on_number_press('6'))
        self.b7.bind(on_press=lambda instance: self.on_number_press('7'))
        self.b8.bind(on_press=lambda instance: self.on_number_press('8'))
        self.b9.bind(on_press=lambda instance: self.on_number_press('9'))
        self.b0.bind(on_press=lambda instance: self.on_number_press('0'))
        self.badd.bind(on_press=lambda instance: self.on_operator_press('+'))
        self.bsub.bind(on_press=lambda instance: self.on_operator_press('-'))
        self.bmul.bind(on_press=lambda instance: self.on_operator_press('*'))
        self.bdiv.bind(on_press=lambda instance: self.on_operator_press('/'))
        self.beq.bind(on_press=self.on_equals_press)
        self.bclr.bind(on_press=self.on_clear)
        self.bback.bind(on_press=self.on_backspace)
        self.expression = ""
        self.output = output

        self.add_widget(self.lrb)
        self.add_widget(self.brb)
        self.add_widget(self.b1)
        self.add_widget(self.b2)
        self.add_widget(self.b3)
        self.add_widget(self.b4)
        self.add_widget(self.b5)
        self.add_widget(self.b6)
        self.add_widget(self.b7)
        self.add_widget(self.b8)
        self.add_widget(self.b9)
        self.add_widget(self.b0)
        self.add_widget(self.badd)
        self.add_widget(self.bsub)
        self.add_widget(self.bmul)
        self.add_widget(self.bdiv)
        self.add_widget(self.beq)
        self.add_widget(self.bclr)
        self.add_widget(self.bback)
        self.add_widget(self.output)


    def on_number_press(self, number):
        self.expression += number
        self.output.text = self.expression

    def on_operator_press(self, operator):
        self.expression += operator
        self.output.text = self.expression

    def on_equals_press(self, instance):
        try:
            result = str(eval(self.expression))
            self.output.text = result
            self.expression = result
        except Exception:
            self.output.text = "Error"
            self.expression = ""

    def on_clear(self, instance):
        self.expression = ""
        self.output.text = ""

    def on_backspace(self, instance):
        self.expression = self.expression[:-1]
        self.output.text = self.expression
    


if __name__ == "__main__":
    MyApp().run()





























