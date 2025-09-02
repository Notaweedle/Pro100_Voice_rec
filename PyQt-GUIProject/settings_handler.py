import os, json

class SettingsHandler():
    def __init__(self, SettingsPage):
        self.SettingsPage = SettingsPage
        # this one will not change
        # otherwise it'd have issues finding where it is to load it :sob:
        self.settings_dir = os.getcwd() + "\\data"
        self.settings_file = self.settings_dir + "\\settings.json"

    def load_settings(self):
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r') as f:
                    settings_json = json.load(f)
                    f.close()
                self.SettingsPage.loadSettings(settings_json)
            except json.JSONDecodeError as e:
                print("Json could not be decoded", e) # have a proper error message window pop up in this case
            except Exception as e:
                print("unknown error!!!!", e) # just catching in case theres other possible errors else i missed
        else:
            # create missing folder (if it doesn't exist)
            if not os.path.exists(self.settings_dir):
                os.makedirs(self.settings_dir)
            # create default settings and append them to json
            default_settings = self.create_default_settings()
            with open(self.settings_file, 'w') as f:
                json.dump(default_settings, f, indent=2)
                f.close()
            self.SettingsPage.loadSettings(default_settings)

    def create_default_settings(self):
        settings = {}

        #input defaults
        input_device = {'name': 'Default', 'index': None}
        settings["input_device"] = input_device
        settings["input_volume"] = 50
        #output defaults
        output_device = {'name': 'Default', 'index': None}
        settings["output_device"] = output_device
        settings["output_volume"] = 50
        #rest of defaults
        settings["text_to_speech"] = False
        settings["pause_threshold"] = 0.8
        settings["speech_model"] = "whisper"
        settings["save_directory"] = os.getcwd() + "\\data"

        return settings

    def save_settings(self, settings):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "w") as f:
                json.dump(settings, f, indent=2)
                f.close()

# _______________________________________________________________________

# Ignore this, just to keep it all together 

def get_tts():
    #yes I know this just loads the settings again, but its needed here
    with open("./data/settings.json", "r") as f: 
        return json.load(f)
