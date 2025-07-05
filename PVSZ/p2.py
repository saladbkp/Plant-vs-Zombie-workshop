import pymem
import pymem.process

def get_pointer_address(pm, base, offsets):
    """Properly resolve multi-level pointer (base -> [offset1] -> [offset2] -> ...)"""
    addr = pm.read_int(base)
    for offset in offsets[:-1]:
        addr = pm.read_int(addr + offset)
    return addr + offsets[-1]

def main():
    pm = pymem.Pymem("popcapgame1.exe")
    base_address = 0x006A9EC0
    offsets = [0x768, 0x144, 0x70]
    first_card_address = get_pointer_address(pm, base_address, offsets)
    print(f"First card slot address: 0x{first_card_address:08X}")

    SLOT_COUNT = 6
    SLOT_SIZE = 0x50

    for i in range(SLOT_COUNT):
        slot_address = first_card_address + (SLOT_SIZE * i)
        current_cd = pm.read_int(slot_address)
        low_16 = current_cd & 0xFFFF # bitwise AND
        # If both bits are 1, the resulting bit in that position is 1.
        # Otherwise (if at least one bit is 0), the resulting bit in that position is 0.

        print(f"Slot {i+1} Address: 0x{slot_address:08X}, Current CD: 0x{current_cd:08X}")

        if low_16 != 0x0001:
            new_cd = (current_cd & 0xFFFF0000) | 0x0001
            pm.write_int(slot_address, new_cd)
            print(f"→ Updated Slot {i+1} CD to 0x{new_cd:08X}")
        else:
            print(f"→ Slot {i+1} already ready")

if __name__ == "__main__":
    main()
