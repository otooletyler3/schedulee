from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
from logger import log
import datetime
import json
import sys

class Schedulee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Schedulee")
        self.resize(1200, 800)
        
        self.setWindowIcon(QIcon('assets/schedulee.png'))

        self.new_session()

        self.settings = {}
        self.load_settings()
        self.load_style_sheet()

    def setup_layout(self):
        pass

    def load_style_sheet(self):
        with open(f'assets/themes/{self.settings["theme"]}.qss', "r") as f:
            style_sheet = f.read()
            self.setStyleSheet(style_sheet)

    def close_window(self, event):

        super().closeEvent(event)

    def new_session(self):
        with open('tmp/session', "w") as f:
            time_now = datetime.datetime.now()
            f.write(time_now.strftime("%Y%m%d%H%M%S"))

    def load_files(self):
        with open('data/settings.json', "r") as f:
            self.settings_json = json.load(f)

        with open('data/valid_settings.json', "r") as f:
            self.valid_settings = json.load(f)

        with open('data/default_settings.json', "r") as f:
            self.default_settings = json.load(f)

    def load_settings(self):       
        self.load_files() 
        self.load_setting("theme")

    def load_setting(self, name, error="default"):
        self.read_setting = self.settings_json[f"{name}"]
        if self.read_setting in self.valid_settings[f"{name}"]:
            self.settings[f"{name}"] = self.settings_json[f"{name}"]
            log(f"Using {self.settings[f"{name}"]} for setting {name}")
        
        else:
            if error == "default":
                self.settings[f"{name}"] = self.default_settings[f"{name}"]
                log(f'No theme found, defaulted {name} to: {self.settings[f"{name}"]}', type="warn")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Schedulee()
    window.show()
    app.exec()