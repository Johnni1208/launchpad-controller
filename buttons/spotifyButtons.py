import subprocess

from buttons.button import Button


class SpotifyMainButton(Button):
    def __init__(self, launchpad):
        super().__init__(launchpad, [3, 0, 127], [0, 51, 0])

    def clicked(self):
        subprocess.Popen(['C:\\Users\\John\\AppData\\Roaming\\Spotify\\spotify.exe'])
        for i in range(0, 3):
            self.blink()
        self.reset_color()
