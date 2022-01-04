from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label_names = {"Mr. Bean", "Johnny English", "Rowan Atkinson"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.label_names:
            temp_label = Label(text=name)
            temp_label.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_label)

    def press_entry(self, instance):
        name = instance.text

    def clear_all(self):
        self.root.ids.entries_box.clear_widgets()


DynamicLabelsApp().run()
