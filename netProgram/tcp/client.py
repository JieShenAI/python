import socket
def main():
    # creat tcp socket
    # stream (tcp)
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server_ip = '192.168.0.102' 
    # server_ip = ('inpput server ip:')
    server_port = 8080
    # server_port = int('input server port')

    server_addr = (server_ip,server_port)

    # link server
    tcp_socket.connect(server_addr)

    # send/recv
    send_data = input('Your msg:')
    tcp_socket.send(send_data.encode('gbk'))

    recvData = tcp_socket.recv(1024)
    print(recvData.decode('gbk'))

    # close
    tcp_socket.close()
if __name__ == "__main__":
    main()
