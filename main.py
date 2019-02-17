import launchpad_py as launchpad
from pygame import time as time

from buttons.youtubeButton import YoutubeButton
from buttons.netflixButton import NetflixButton
from buttons.spotifyButton import SpotifyMainButton
from buttons.media.playAndPauseButton import PlayAndPauseButton
from buttons.media.nextTrackButton import NextTrackButton
from buttons.media.previousTrackButton import PreviousTrackButton


lp = launchpad.LaunchpadMk2()
if lp.Open(0, "mk2"):
    print(" - Launchpad Mk2: Ok")
else:
    print(" - Launchpad Mk2: Could not find Launchpad")
lp.ButtonFlush()

lp.LedAllOn(500)
time.wait(500)
lp.LedAllOn(0)

# Init youtube button
ytButton = YoutubeButton(lp)

# Init Netflix button
netflixButton = NetflixButton(lp)

# Init Spotify button
spotifyButton = SpotifyMainButton(lp)

# Init Play / Pause Button
playPauseButton = PlayAndPauseButton(lp)

# Init Next Track Button
nextTrackButton = NextTrackButton(lp)

# Init Previous Track Button
prevTrackButton = PreviousTrackButton(lp)

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

        if clickedButton == playPauseButton.get_position():
            playPauseButton.clicked()

        if clickedButton == nextTrackButton.get_position():
            nextTrackButton.clicked()

        if clickedButton == prevTrackButton.get_position():
            prevTrackButton.clicked()

        # Cancel program
        if clickedButton == [8, 8, 127]:
            lp.LedAllOn(79)
            time.wait(500)
            lp.Reset()
            break

lp.Close()
