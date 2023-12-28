import socket
import time

# Steps
# 1. Device Manager -> Realtek Bluetooth Adapter
# 2. Right Click -> Properties -> Advanced -> Address
# 3. Turn on Bluetooth on both devices and make server device visible

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)  # RFCOMM specific protocol
server.bind(("D8:3A:DD:18:15:40", 4))  # MAC Address and Channel 4

server.listen(1)

print("Waiting for connection...")

client, addr = server.accept()
print(f"Accepted connection from {addr}")

try:
    for i in range(10000):
            message = f"ID: {i}"
            print(f"Send: {message}")
            client.send(message.encode('utf-8'))
            time.sleep(1)

except OSError:
    pass

print("Disconnected")

client.close()
server.close()