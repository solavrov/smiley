from kivy.uix.boxlayout import BoxLayout


class Layout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.widget = None

    def place_widget(self, widget):
        self.clear_widgets()
        self.add_widget(widget)


