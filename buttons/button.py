from pygame import time as time
import launchpad_py
from abc import abstractmethod


class Button:
    __MAP_POSITION = ['x', 'y', 'onOff']

    def __init__(self, launchpad, position, color):
        self.lp = launchpad
        self._POSITION = {
            'x': position[0],
            'y': position[1],
            'onOff': 127
        }
        self.COLOR = color
        self.reset_color()

    @abstractmethod
    def clicked(self):
        pass

    def get_position(self):
        return list(map(self._POSITION.get, self.__MAP_POSITION))

    def blink(self, blink_time=0.5, blink_count=3):
        blink_time = int(blink_time * 1000)

        for i in range(0, blink_count):
            self.lp.LedCtrlXYByCode(self._POSITION['x'], self._POSITION['y'], launchpad_py.LaunchpadPro.COLORS['white'])
            time.wait(blink_time)

            self.lp.LedCtrlXYByCode(self._POSITION['x'], self._POSITION['y'], launchpad_py.LaunchpadPro.COLORS['black'])
            time.wait(blink_time)
        self.reset_color()

    def reset_color(self):
        self.lp.LedCtrlXYByRGB(self._POSITION['x'], self._POSITION['y'], self.COLOR)
