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
scan on
discoverable on

# RPI BT always on discoverable
sudo apt install bluetooth bluez bluez-tools
sudo nano /etc/bluetooth/main.conf
Name = RaspberryPi
sudo nano /lib/systemd/system/bluetooth.service
ExecStart=/usr/lib/bluetooth/bluetoothd -C
sudo systemctl restart bluetooth
sudo reboot