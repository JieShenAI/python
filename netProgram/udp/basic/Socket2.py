import socket

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #Send data cyclically   
    while(True):

        #input data
        send_data = input('please input your data:')

        if send_data == "exit":
            break

        #send and receive data, part2 ("ip",port) 

        udp_socket.sendto(send_data.encode('utf-8'),("192.168.0.102",8080))

    #close socket
    udp_socket.close()

    print('run')
if __name__ == "__main__":
    main()
