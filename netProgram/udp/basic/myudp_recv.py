import socket
def main():

    # creat socket
    #udp_socket = socket.socket(socket.AF_INEF,socket.SOCK_DGRAM)
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # bind ip:port
    # as you know ,if you want to receive data,if must have a fixed port
    localaddr = ('',7788)
    udp_socket.bind(localaddr)
    while(True):
        # receive data
        recv_data = udp_socket.recvfrom(1024)  #1024 is the max len,I receive once.
        
        # print
        
        recv_msg = recv_data[0]
        send_addr = recv_data[1]  #ip address of sender
        # don't decode by 'utf-8',windows encode is 'gbk',you can try Chinese words to see it.
        # linux encode is 'utf-8'
        print("%s:%s"%(send_addr,recv_msg.decode('gbk')))
    
    #close socket
    udp_socket.close()

if __name__ == '__main__':
    main()

