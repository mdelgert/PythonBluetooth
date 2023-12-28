# PythonBluetooth

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

# Setup BT
bluetoothctl
power on
discoverable on
pairable on

# Scan for devices
scan on

# RPI BT always on discoverable
sudo apt install bluetooth bluez bluez-tools
sudo nano /etc/bluetooth/main.conf
Name = RaspberryPi
DiscoverableTimeout = 0
sudo systemctl daemon-reload;
sudo systemctl restart bluetooth.service;

# Bring NT online
sudo hciconfig -a
sudo hciconfig hci0 up
sudo bluetoothctl
agent on

# Example /etc/rc.local does not work use bluetooth_discoverable.sh
# sudo bluetoothctl <<EOF
# power on
# discoverable on
# pairable on
# EOF
# sudo hciconfig hci0 piscan &