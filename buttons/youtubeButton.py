import webbrowser

from .button import Button


class YoutubeButton(Button):
    def __init__(self, launchpad):
        super().__init__(launchpad, [0, 0, 127], [255, 0, 0])

    def clicked(self):
        webbrowser.open('https://youtube.com')
        for i in range(0, 3):
            self.blink()
        self.reset_color()

