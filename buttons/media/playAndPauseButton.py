from buttons.button import Button
from pyautogui import press
import launchpad_py


class PlayAndPauseButton(Button):
    isRed = False

    def __init__(self, launchpad):
        super().__init__(launchpad, [3, 1], [0, 51, 0])

    def clicked(self):
        press('playpause')
        self.switch_color()

    def switch_color(self):
        if self.isRed:
            self.lp.LedCtrlXYByRGB(self._POSITION['x'], self._POSITION['y'], self.COLOR)
            self.isRed = False
            return
        self.lp.LedCtrlXYByCode(self._POSITION['x'], self._POSITION['y'], launchpad_py.LaunchpadPro.COLORS['red'])
        self.isRed = True
