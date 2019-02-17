import launchpad_py as launchpad
from pygame import time as time
import random
import webbrowser
import subprocess

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

# Set Youtube Button Red
lp.LedCtrlXYByRGB(0, 0, [255, 0, 0])
YOUTUBE_BUTTON = [0, 0, 127]
# Set Netflix Button Dark Red
lp.LedCtrlXYByRGB(1, 0, [0, 153, 51])
NETFLIX_BUTTON = [1, 0, 127]

# Set Spotify Button Green
lp.LedCtrlXYByRGB(3, 0, [0, 51, 0])
SPOTIFY_BUTTON = [3, 0, 127]

while True:
    buts = lp.ButtonStateXY()
    if buts and buts[2] == 127:
        # x = buts[0]
        # y = buts[1]
        # lp.LedCtrlXYByCode(x, y, random.randint(4, 100))
        # if buts == [8, 7, 127]:
        #     lp.Reset()

        if buts == YOUTUBE_BUTTON:
            webbrowser.open('https://youtube.com')
            for i in range(0, 3):
                lp.LedCtrlXYByCode(YOUTUBE_BUTTON[0], YOUTUBE_BUTTON[1], 3)
                time.wait(500)
                lp.LedCtrlXYByCode(YOUTUBE_BUTTON[0], YOUTUBE_BUTTON[1], 0)
                time.wait(500)
            lp.LedCtrlXYByRGB(YOUTUBE_BUTTON[0], YOUTUBE_BUTTON[1], [255, 0, 0])

        if buts == NETFLIX_BUTTON:
            webbrowser.open('https://netflix.com')
            for i in range(0, 3):
                lp.LedCtrlXYByCode(NETFLIX_BUTTON[0], NETFLIX_BUTTON[1], 3)
                time.wait(500)
                lp.LedCtrlXYByCode(NETFLIX_BUTTON[0], NETFLIX_BUTTON[1], 0)
                time.wait(500)
            lp.LedCtrlXYByRGB(NETFLIX_BUTTON[0], NETFLIX_BUTTON[1], [0, 153, 51])

        if buts == SPOTIFY_BUTTON:
            subprocess.Popen(['C:\\Users\\John\\AppData\\Roaming\\Spotify\\spotify.exe'])
            for i in range(0, 3):
                lp.LedCtrlXYByCode(SPOTIFY_BUTTON[0], SPOTIFY_BUTTON[1], 3)
                time.wait(500)
                lp.LedCtrlXYByCode(SPOTIFY_BUTTON[0], SPOTIFY_BUTTON[1], 0)
                time.wait(500)
            lp.LedCtrlXYByRGB(SPOTIFY_BUTTON[0], SPOTIFY_BUTTON[1], [0, 51, 0])

        if buts == [8, 8, 127]:
            lp.LedAllOn(79)
            time.wait(500)
            lp.Reset()
            break

lp.Close()
