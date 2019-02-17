from pygame import time as time
import launchpad_py


class Button:
    __MAP_POSITION = ['x', 'y', 'onOff']

    def __init__(self, launchpad, position, color):
        self.lp = launchpad
        self.__POSITION = {
            'x': position[0],
            'y': position[1],
            'onOff': position[2]
        }
        self.COLOR = color
        self.reset_color()

    def get_position(self):
        return list(map(self.__POSITION.get, self.__MAP_POSITION))

    def blink(self):
        self.lp.LedCtrlXYByCode(self.__POSITION['x'], self.__POSITION['y'], launchpad_py.LaunchpadPro.COLORS['white'])
        time.wait(500)

        self.lp.LedCtrlXYByCode(self.__POSITION['x'], self.__POSITION['y'], launchpad_py.LaunchpadPro.COLORS['black'])
        time.wait(500)

    def reset_color(self):
        self.lp.LedCtrlXYByRGB(self.__POSITION['x'], self.__POSITION['y'], self.COLOR)
