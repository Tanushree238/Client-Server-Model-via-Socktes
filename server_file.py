import socket

HOST = "127.0.0.1"
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen()

while True:
    connection, address = server_socket.accept()
    print("Connected to", address)
    while True:
        data = connection.recv(1024)
        if not data:
            break
        connection.sendall(data)
    connection.close()
    print("Disconnected with", address)

server_socket.close() 

  
  