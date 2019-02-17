from buttons.button import Button
from pyautogui import press


class NextTrackButton(Button):

    def __init__(self, launchpad):
        super().__init__(launchpad, [4, 1], [0, 25, 0])

    def clicked(self):
        press('nexttrack')
        self.blink(0.25, 1)
