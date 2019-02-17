import webbrowser

from .button import Button


class NetflixButton(Button):
    def __init__(self, launchpad):
        super().__init__(launchpad, [1, 0, 127], [0, 153, 51])

    def clicked(self):
        webbrowser.open('https://netflix.com')
        for i in range(0, 3):
            self.blink()
        self.reset_color()

