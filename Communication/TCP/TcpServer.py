import TcpNet

Tcp = TcpNet.TcpNet()
Tcp.Accept('192.168.10.6', 20004)
print ('connected ...')

while True:
    print(Tcp.ReceiveStr())
    send_data = input ('Reply : ')
    Tcp.SendStr(send_data)