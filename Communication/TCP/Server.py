import socket

com_socket = socket.socket()
com_socket.bind(('192.168.10.6', 20002))
com_socket.listen(10)
connection, address = com_socket.accept()

print (address, 'connected ... !')

while True:
    print (connection.recv(4096).decode("UTF-8"))
    send_data = input ("Reply : ")
    connection.send(bytes(send_data, "UTF-8"))

