import launchpad_py as launchpad
from pygame import time as time
from buttonsController import setup_buttons

lp = launchpad.LaunchpadMk2()

# Tests if Launchpad is connected
if lp.Open(0, "mk2"):
    print(" - Launchpad Mk2: Ok")
else:
    print(" - Launchpad Mk2: Could not find Launchpad")

# Flushes the Launchpad, in case of it having anything saved
lp.ButtonFlush()

# Shows a short orange flash so the user sees that the program is ready
lp.LedAllOn(500)
time.wait(500)
lp.LedAllOn(0)

# Sets up all buttons
setup_buttons(lp)

# If the program gets terminated close the Launchpad connection
lp.Close()
