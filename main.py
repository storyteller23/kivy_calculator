from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.operators = ['/', '*', '+', '-', '%', '**']
        self.ns_operators = ['toBin', 'toHex']
        self.title = 'Calculator'
        self.last_was_operator = None
        self.last_button = None
        self.last_was_ns_operation = None

        main_layout = BoxLayout(orientation='vertical')
        self.solution = TextInput(background_color='white', foreground_color='black', multiline=True, halign='right',
                                  font_size=170, readonly=True, height=55)

        main_layout.add_widget(self.solution)
        buttons = [
            ['(', ')', 'toBin', 'toHex'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '+'],
            ['.', '0', 'C', '-'],
            ['%', '**', 'π', '<-X'],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label, font_size=85, background_color='white',
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equal_button = Button(
            text='=', font_size=85, background_color='white',
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
        )
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    def on_button_press(self, instance):
        if self.solution.text == 'Error':
            self.solution.text = ''

        current = self.solution.text
        button_text = instance.text

        if button_text == 'C' or self.last_was_ns_operation:
            self.last_was_ns_operation = None
            self.solution.text = ''
        elif button_text == '<-X':
            self.solution.text = self.solution.text[:-1]
        elif button_text == 'π':
            self.solution.text += '3,141592'
        else:
            if current and (self.last_was_operator and (button_text in self.operators or button_text in self.ns_operators)):
                return
            elif current == '' and (button_text in self.operators or button_text in self.ns_operators):
                return
            elif current and button_text in self.ns_operators:
                if button_text == 'toBin':
                    self.solution.text = str(eval(f'str(bin({current}))[2:]'))
                elif button_text == 'toHex':
                    self.solution.text = str(eval(f'str(hex({current}))[2:].upper()'))

            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
        self.last_was_ns_operation = button_text in self.ns_operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                solution = str(round(eval(self.solution.text), 5))
                self.solution.text = solution
            except:
                self.solution.text = 'Error'


if __name__ == '__main__':
    CalculatorApp().run()
