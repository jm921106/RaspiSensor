import os

class SndPort:
    def pFileSend(self, FileName, bDta):
        sze = len (bDta)
        btsend = bytearray()
        btsend.append(0x4a)
        btsend.append(0x12)
        btsend.append(0x8b)
        btsend.append(0x13)
        flesze = len(FileName)
        sze += (flesze + 1)
        hsze = int(sze/0x1000000)

        btsend.append(hsze)
        hsze = sze = hsze*-0x1000000