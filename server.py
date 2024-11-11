#Melina Khaleghi

import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            break
    client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(1)
    client_socket, addr = server_socket.accept()
    print(addr)
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
    while True:
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))

start_server()
