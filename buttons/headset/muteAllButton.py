from buttons.button import Button
from pyautogui import press


class MuteAllButton(Button):
    def __init__(self, launchpad):
        super().__init__(launchpad, [8, 6], [255, 100, 0])

    def clicked(self):
        press('pause')
        self.blink(0.25, 1)
