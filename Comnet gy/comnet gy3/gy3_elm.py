import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost',10000))
sock.listen(1)

connection, client_address = sock.accept()
connection.send("Hello!".encode())
connection.close()
    
data = connection.recv(16)

print(data.decode())




