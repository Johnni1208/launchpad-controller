from buttons.button import Button
from pyautogui import press


class MuteVoiceButton(Button):
    def __init__(self, launchpad):
        super().__init__(launchpad, [8, 7], [255, 100, 0])

    def clicked(self):
        press('scrolllock')
        self.blink(0.25, 1)
