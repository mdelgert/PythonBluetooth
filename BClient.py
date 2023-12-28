import bluetooth

def start_client():
    server_address = "D8:3A:DD:23:71:88"  # Replace with the server's Bluetooth address
    port = 1

    client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_socket.connect((server_address, port))

    print("Connected to the server. Type 'exit' to end the chat.")

    while True:
        message = input("Enter message: ")
        if message.lower() == "exit":
            break
        client_socket.send(message)

    client_socket.close()

if __name__ == "__main__":
    start_client()
