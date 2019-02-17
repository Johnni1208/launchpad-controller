import webbrowser

from .button import Button


class YoutubeButton(Button):
    def __init__(self, launchpad):
        super().__init__(launchpad, [0, 0], [255, 0, 0])

    def clicked(self):
        webbrowser.open('https://youtube.com')
        self.blink()
