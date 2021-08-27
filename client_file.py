import socket 

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST,PORT))
    client_socket.sendall(b'Hello World')
    data = client_socket.recv(1024)

print("Recieved Data - ", repr(data))
