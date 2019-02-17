import launchpad_py as launchpad
from pygame import time as time

from buttons.youtubeButton import YoutubeButton
from buttons.netflixButton import NetflixButton
from buttons.spotifyButtons import SpotifyMainButton


lp = launchpad.LaunchpadMk2()
if lp.Open(0, "mk2"):
    print(" - Launchpad Mk2: Ok")
else:
    print(" - Launchpad Mk2: Could not find Launchpad")
lp.ButtonFlush()

print(" - Testing LedAllOn()")
for i in [5, 21, 79, 3]:
    lp.LedAllOn(i)
    time.wait(500)
lp.LedAllOn(0)
print(" - Test successfully")

# Init youtube button
ytButton = YoutubeButton(lp)

# Set Netflix Button Dark Red
netflixButton = NetflixButton(lp)

# Set Spotify Button Green
spotifyButton = SpotifyMainButton(lp)

while True:
    clickedButton = lp.ButtonStateXY()
    if clickedButton and clickedButton[2] == 127:
        # x = buts[0]
        # y = buts[1]
        # lp.LedCtrlXYByCode(x, y, random.randint(4, 100))
        # if buts == [8, 7, 127]:
        #     lp.Reset()

        if clickedButton == ytButton.get_position():
            ytButton.clicked()

        if clickedButton == netflixButton.get_position():
            netflixButton.clicked()

        if clickedButton == spotifyButton.get_position():
            spotifyButton.clicked()

        if clickedButton == [8, 8, 127]:
            lp.LedAllOn(79)
            time.wait(500)
            lp.Reset()
            break

lp.Close()
