from buttons.button import Button
from pyautogui import press


class PreviousTrackButton(Button):

    def __init__(self, launchpad):
        super().__init__(launchpad, [2, 1], [0, 25, 0])

    def clicked(self):
        press('prevtrack')
        self.blink(0.25, 2)
