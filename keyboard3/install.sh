#!/usr/bin/env bash

# If this is run from SSH, your connection will disconnect when this script is done.

#git clone https://github.com/mdelgert/pizero-usb-hid-keyboard
#cd pizero-usb-hid-keyboard
#gcc hid-gadget-test.c -o hid-gadget-test
./setup-hid-modules.sh
./enableHIDRCLocal.sh
poweroff