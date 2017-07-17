import TcpNet

Tcp = TcpNet.TcpNet()
Tcp.Connect('192.168.10.6', 20002)
print ('connected ...')

while True:
    send_data = inpit ( 'message : ')
    Tcp.SendStr(send_data)
    print(Tcp.ReceiveStr())