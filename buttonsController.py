from pygame import time as time

from buttons.youtubeButton import YoutubeButton
from buttons.netflixButton import NetflixButton
from buttons.spotifyButton import SpotifyMainButton
from buttons.media.playAndPauseButton import PlayAndPauseButton
from buttons.media.nextTrackButton import NextTrackButton
from buttons.media.previousTrackButton import PreviousTrackButton

from buttons.headset.muteVoiceButton import MuteVoiceButton
from buttons.headset.muteAllButton import MuteAllButton


def setup_buttons(lp):
    ytButton = YoutubeButton(lp)
    netflixButton = NetflixButton(lp)
    spotifyButton = SpotifyMainButton(lp)
    playPauseButton = PlayAndPauseButton(lp)
    nextTrackButton = NextTrackButton(lp)
    prevTrackButton = PreviousTrackButton(lp)
    muteVoiceButton = MuteVoiceButton(lp)
    muteAllButton = MuteAllButton(lp)

    # Loop for checking if a button got pressed
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

            if clickedButton == muteVoiceButton.get_position():
                muteVoiceButton.clicked()

            if clickedButton == muteAllButton.get_position():
                muteAllButton.clicked()

            # Cancel program
            if clickedButton == [8, 8, 127]:
                lp.LedAllOn(79)
                time.wait(500)
                lp.Reset()
                break
