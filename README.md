# Make Linux System Discoverable by Remote Bluetooth Devices
https://www.instructables.com/Turn-the-Raspberry-Pi-into-a-Bluetooth-Device/
https://www.instructables.com/Make-Raspberry-Pi-Discoverable-By-Remote-Bluetooth/

# Using Raspberry Pi 3 On-Board Bluetooth for Communication
https://www.electronicwings.com/raspberry-pi/using-raspberry-pi-3-on-board-bluetooth-for-communication

# Using Python For Bluetooth
https://ukbaz.github.io/howto/bluetooth_overview.html
https://github.com/ukBaz/python-bluezero/wiki

# PythonBluetooth
https://github.com/pybluez/pybluez/tree/master
https://github.com/hbldh/bleak/tree/develop
https://github.com/kevincar/bless

# Bluetooth Programming with Python 3
http://blog.kevindoran.co/bluetooth-programming-with-python-3/

# Links
https://www.youtube.com/watch?v=8pMaR-WUc6U
https://github.com/NeuralNine/youtube-tutorials
https://github.com/NeuralNine/youtube-tutorials/tree/main/Bluetooth%20Chat
https://github.com/pybluez/pybluez/issues/431
https://github.com/AnesBenmerzoug/Bluetooth_HID
https://github.com/DGTCentaurMods/DGTCentaurMods/issues/98
https://stackoverflow.com/questions/34599703/rfcomm-bluetooth-permission-denied-error-raspberry-pi
https://medium.com/cemac/keep-bluetooth-discoverable-rpi-unix-bbe1c9ecbdb6
https://www.cnet.com/tech/computing/how-to-setup-bluetooth-on-a-raspberry-pi-3/
https://www.slashgear.com/1275647/raspberry-pi-4-how-to-enable-pair-bluetooth/
https://unix.stackexchange.com/questions/205321/where-should-i-put-hciconfig-hci0-up-for-start-up
https://raspberry-projects.com/pi/pi-operating-systems/raspbian/bluetooth/bluetooth-commands
https://raspberrypi.stackexchange.com/questions/14598/making-raspberry-pi-bluetooth-slave/19865#19865
https://stackoverflow.com/questions/62652901/how-do-i-broadcast-bluetooth-inquiry-with-python-sockets-af-bluetooth-socket
https://gist.github.com/scientificRat/be2bbac0769bfa04820bc73edc009bdf
https://roboticsknowledgebase.com/wiki/networking/bluetooth-sockets/

# PiKVM Bluetooth HID
https://docs.pikvm.org/bluetooth_hid/
https://github.com/pikvm/kvmd/tree/master/hid

# Mouse keyboard for Raspberry Pi Pico
https://github.com/argilo/pico-jiggler
https://github.com/stjeong/rasp_vusb

# Simple bluetooth keyboard with Raspberry PI
https://tailcall.net/posts/bluetooth-keyboard/
https://github.com/msm-code/RandomCodes/tree/master/bluetooth-keyboard
https://gist.github.com/ukBaz/a47e71e7b87fbc851b27cde7d1c0fcf0

# Pair 2 Raspberry Pis
https://bluedot.readthedocs.io/en/latest/pairpipi.html

# Setup
sudo apt install python3-pip
pip install virtualenv
python -m virtualenv venv
pip install pybluez2 pyautogui

# Windows
venv\Scripts\activate

# Linux
source venv/bin/activate

# RPI4 enable bluetooth
sudo systemctl enable bluetooth
sudo systemctl start bluetooth
sudo systemctl restart bluetooth
systemctl status bluetooth
hciconfig
bluetoothd -v

# RPI BT always on discoverable
sudo nano /etc/bluetooth/main.conf
sudo systemctl daemon-reload
sudo systemctl restart bluetooth.service

# Bring BT online manually
sudo hciconfig hci0 up
sudo hciconfig -a
sudo bluetoothctl
power on
discoverable on
pairable on
agent on

# Scan for devices
scan on