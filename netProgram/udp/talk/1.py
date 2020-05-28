import socket

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #input ip and port of other individual
    
    dest_ip = input("Other individual ip:")
    # int !!!
    dest_port = int(input('Other individual port:'))


    #Send data cyclically   
    #while(True):

    #input data
    send_data = input('please input your data:')

    #if send_data == "exit":
        #break

    #send and receive data, part2 ("ip",port) 

    udp_socket.sendto(send_data.encode('utf-8'),(dest_ip,dest_port))

    #receive data
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)

    #close socket
    udp_socket.close()

    print('run')
if __name__ == "__main__":
    main()
