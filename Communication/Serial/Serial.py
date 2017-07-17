import Rs232
Srl = Rs232.Rs232(9600)
bte = bytearray()

for i in range(0, 256):
    bte.append(i)

Srl.Send(bte)

while True:
    dta = Srl.Receive()
    if dta != None:
        break

print(data)