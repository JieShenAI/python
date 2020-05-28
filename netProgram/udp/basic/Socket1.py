import socket

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #send and receive data, part2 ("ip",port) 

    udp_socket.sendto(b"hahaha----01",("192.168.0.102",8080))

    #close socket
    udp_socket.close()

    print('run')
if __name__ == "__main__":
    main()
