import socket
import struct



def client_prog():
    host = 'localhost'  # as both code is running on same pc
    port = 10000  # socket server port number


    int_one = int(input("int 1 -> "))  # take input
    operator = (input("operator -> ")).encode()
    int_two = int(input("int 2 -> "))  # take input
    
    vals = (int_one, operator, int_two)
    
    packer = struct.Struct('i s i')
    
    packed_data = packer.pack(*vals)
    
    c_sock = socket.socket()  # instantiate
    c_sock.connect((host, port))  # connect to the server
    

    while str(int_one).lower().strip() != 'bye':
        print(vals)
        c_sock.send(packed_data)  # send message
        data = c_sock.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal

        int_one_new = int(input("int 1 -> "))  # take input
        operator_new = (input("operator -> ")).encode()
        int_two_new = int(input("int 2 -> "))  # take input
        
        vals = (int_one_new, operator_new, int_two_new)
        packed_data = packer.pack(*vals)
        c_sock.send(packed_data)  # send message

    c_sock.close()  # close the connection


if __name__ == '__main__':
    client_prog()