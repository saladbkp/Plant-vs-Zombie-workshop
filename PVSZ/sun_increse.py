import pymem
import pymem.process

print("hello word")
pm = pymem.Pymem("popcapgame1.exe")
base_addr = 0x06A9EC0
offset1 = 0x768
offset2 = 0x5560


address1 = pm.read_int(base_addr)
print("addr1",hex(address1))
address2 = pm.read_int(address1+offset1)
print("addr2",hex(address2))
sunn_addr = address2+offset2
print("sun",hex(sunn_addr))
address3 = pm.read_int(address2+offset2)
print("addr3",address3)
while(True):
    pm.write_int(sunn_addr,9999)