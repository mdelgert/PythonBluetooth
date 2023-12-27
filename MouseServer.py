import bluetooth
import pyautogui

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

client_sock, address = server_sock.accept()
print("Connected to client:", address)

while True:
    data = client_sock.recv(1024)  # Receive control signal
    if data == b"jiggle":
        pyautogui.moveRel(1, 0)  # Jiggle the mouse
        pyautogui.moveRel(-1, 0)

client_sock.close()
server_sock.close()