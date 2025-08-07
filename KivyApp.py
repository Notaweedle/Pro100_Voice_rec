import kivy

from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from VoiceToSpeech import listen_short

class Kivy(FloatLayout):
    label_wid = ObjectProperty()
    info = StringProperty()
    speech_occurring = BooleanProperty()

    def do_action(self):
        recorded_speech = listen_short()
        self.label_wid.text = 'pressed!'
        self.info = 'updated text'
        print(recorded_speech)

    def start_speech(self):
        if not self.speech_occurring:
            self.speech_occurring = True

    def stop_speech(self):
        if self.speech_occurring:
            self.speech_occurring = False

class KivyApp(App):
    def build(self):
        return Kivy(info="Hello, world!")

if __name__ == '__main__':
    KivyApp().run()
