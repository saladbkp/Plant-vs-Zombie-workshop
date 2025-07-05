import pymem
import pymem.process

def sun():
    print("hello world")
    pm = pymem.Pymem('popcapgame1.exe')
    base_address = 0x006A9EC0
    offset1 = 0x768
    offset2 = 0x5560
    address1 = pm.read_int(base_address)
    address2 = pm.read_int(address1+offset1)
    sun_address = address2+offset2
    current_sun_value = pm.read_int(sun_address)
    print("sun address", current_sun_value)
    pm.write_int(sun_address,99999)
    print("ALL good")

def cd():
    print("hello world")
    pm = pymem.Pymem('popcapgame1.exe')
    base_address = 0x006A9EC0
    offset1 = 0x768
    offset2 = 0x144
    offset3 = 0x70
    address1 = pm.read_int(base_address)
    address2 = pm.read_int(address1+offset1)
    address3 = pm.read_int(address2+offset2)
    address4 = address3 + offset3
    SLOT = 6
    SLOT_SIZE = 0x50
    for s in range(SLOT):
        slot_address = address4 + (SLOT_SIZE*s)
        print("slot address",hex(slot_address))
        current_cd = pm.read_int(slot_address)
        print(f"Slot {s+1} Address: 0x{slot_address:08X}, Current CD: 0x{current_cd:08X}")
        low_16 = current_cd & 0xFFFF

        if low_16 != 0x0001:
            new_cd = (current_cd & 0xFFFF0000) | 0x0001
            pm.write_int(slot_address, new_cd)
            print(f"→ Updated Slot {s+1} CD to 0x{new_cd:08X}")
        else:
            print(f"→ Slot {s+1} already ready")

cd()