#from socket import *
import socket
def main():

    # 1.creat socket
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.bind ip and port

    tcp_server_socket.bind(('',7890))


    # 3.listen,accept return a tuple
    # listening socket only wait for client first linking ,data stream is in a new socket.
    # first variable is a new socket
    # second variable is a client's address

    tcp_server_socket.listen(128)  #what is 128 meaning?

    # 4.accept client's liniking (wait for client's linking)
    new_client_socket,client_addr = tcp_server_socket.accept()
    print(client_addr)

    # 5.recv/send data
    recv_data = new_client_socket.recv(1024)
    print(recv_data)
    
    # sendto client
    new_client_socket.send("hahaha".encode('utf-8'))

    #close two sockets
    new_client_socket.close()
    tcp_server_socket.close()
    


if __name__ == "__main__":
    main()
