import threading
import socket

HOST = ''
PORT = 1379

clients = []

def handle_client(client_socket, client_address):
    print(f"Connected to {client_address}")
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Received from {client_address}")

            for sock in clients:
                if sock != client_socket:
                    sock.sendall(message.encode())
        except:
            break

    print(f"Disconnected from {client_address}")
    clients.remove(client_socket)
    client_socket.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on port {PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
