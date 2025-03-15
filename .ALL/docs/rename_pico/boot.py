# Renaming CIRCUITPY through CircuitPython
#
# You can also rename the board using CircuitPython. Create a new file on your CIRCUITPY drive called boot.py. Copy the following code into the new boot.py file:

import storage

storage.remount("/", readonly=False)

m = storage.getmount("/")
m.label = "NEW_NAME"

storage.remount("/", readonly=True)

storage.enable_usb_drive()

# Eject your board, and reboot the board either by pressing the reset button once, or unplugging it and plugging it back in. After a moment, it should show up in your file explorer with the NEW_NAME you chose for it! You can delete boot.py after the newly named board shows up in your file explorer.
