# sudo apt-get update
# sudo apt-get install python3
# sudo apt-get install python3-pip
# sudo apt-get install python3-bluez

import bluetooth

def start_server():
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    port = 1  # You can use any available port

    server_socket.bind(("", port))
    server_socket.listen(1)

    print(f"Waiting for connection on RFCOMM channel {port}...")

    client_socket, address = server_socket.accept()
    print(f"Accepted connection from {address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode('utf-8')}")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
