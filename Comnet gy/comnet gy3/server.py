import socket
import struct


def server_prog():
    host = 'localhost'
    port = 10000  

    s_sock = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    s_sock.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    s_sock.listen(2)
    
    packer = struct.Struct('i s i')
    
    conn, address = s_sock.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024)
        if not data:
            # if data is not received break
            break
        
        data_back = packer.unpack(data)
        
        operator = data_back[1].decode()
                
        firstInt = int(data_back[0])
        secondInt = int(data_back[2])
        
        print(firstInt)
        print(secondInt)
        
        
        match operator:
            case '+':
                 conn.send(str(firstInt+secondInt).encode())
            case '-':
                 conn.send(str(firstInt-secondInt).encode())
            case '*':
                 conn.send(str(firstInt*secondInt).encode())
            case '/':
                 conn.send(str(firstInt/secondInt).encode())
                

    conn.close()  # close the connection


if __name__ == '__main__':
    server_prog()