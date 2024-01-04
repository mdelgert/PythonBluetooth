#!/usr/bin/python3

import os
import select
import time
from datetime import datetime

"""Suppress screen savers by periodically toggling Caps Lock

https://gist.githubusercontent.com/davesteele/276a17315cff728bb5932c59329da850/raw/f3b4912418679e095be82a81acd05d557448449c/tickle.py

See https://davesteele.github.io/raspberrypi/2021/04/18/keyboard-jiggler/

Intended to be run on a Gadget Tools-generated device, which configurres a USB
port to run as a USB client.

This periodically sends two Caps Lock key presses, in quick succession, to the
remote host.

This requires an installed pizero-usb-hid-keyboard environment [1], which
creates a virtual keyboard USB client.

[1]: https://github.com/raspberrypisig/pizero-usb-hid-keyboard

"""

# keycodes - 
# https://github.com/raspberrypisig/pizero-usb-hid-keyboard/blob/master/hid-gadget-test.c#L32
KEYCODE = 0x39
GDEV = "/dev/hidg0"
#DELAYSECS = 55
DELAYSECS = 180


def capstoggle():
    """Send two Caps Lock key presses in quick succession."""

    press = bytearray([0, 0, KEYCODE, 0, 0, 0, 0, 0])
    release = bytearray([0, 0, 0, 0, 0, 0, 0, 0])

    fd = None

    try:
        fd = os.open(GDEV, os.O_RDWR)
        for _ in range(2):
            for msg in (press, release):
                os.write(fd, msg)
    except Exception:
        print("Error writing device")
    finally:
        if fd is not None:
            os.close(fd)

def main():
    while True:
        print(f"Tickle ran at: {datetime.now()}")
        capstoggle()
        time.sleep(DELAYSECS)
        
if __name__ == "__main__":
    main()