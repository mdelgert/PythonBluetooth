https://www.instructables.com/Make-Raspberry-Pi-Discoverable-By-Remote-Bluetooth/

sudo hciconfig hci0 piscan
sudo hciconfig -a hci0 | grep -i 'PSCAN *ISCAN'