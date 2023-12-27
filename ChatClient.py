import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
#client.connect(("<MAC address of the PC you are connecting to>", 4))
client.connect(("54:6c:eb:a1:32:44", 4))
#client.connect(("D8:3A:DD:18:15:40", 4))

print(f"Connected!")

try:
    while True:
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))
        data = client.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode('utf-8')}")

except OSError:
    pass

print("Disconnected")

client.close()