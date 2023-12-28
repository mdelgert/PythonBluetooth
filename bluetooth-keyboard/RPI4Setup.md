sudo apt-get install python3-dbus
sudo pip install evdev
sudo service bluetooth stop
sudo nano /lib/systemd/system/bluetooth.service

# Example bluetooth.service
ExecStart=/usr/lib/bluetooth/bluetoothd -P input