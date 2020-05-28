import socket


def send_msg(udp_socket):
    # send
    dest_ip = input("Your talker's ip:")
    dest_port = int(input("port:"))
    send_data = input("Your message:")
    udp_socket.sendto(send_data.encode('utf-8'),(dest_ip,dest_port))


def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    #print("%s:%s" % (str(recv_data[1][0],recv_data[0].decode('utf-8'))))
    print(recv_data)



def main():
    # 1.creat socket
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # bind port
    local_addr = ('',7788)
    udp_socket.bind(local_addr)


    while(True):
        
        send_msg(udp_socket)
        
        recv_msg(udp_socket)

        # receive




if __name__ == "__main__":
    main()
