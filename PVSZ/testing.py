import pymem
import pymem.process
import time

def get_pointer_address(pm, base, offsets):
    """Properly resolve multi-level pointer (base -> [offset1] -> [offset2])"""
    addr = pm.read_int(base)
    print("addr",hex(addr))
    for offset in offsets[:-1]:
        print("offset",hex(offset))
        addr = pm.read_int(addr + offset)
        print("addr",hex(addr))
        print("added",hex(addr + offsets[-1]))
    return addr + offsets[-1]

def main():
    # Attach to process
    pm = pymem.Pymem("popcapgame1.exe")  # Name of Plants vs Zombies process
    base_address = 0x006A9EC0  # Known static base address
    offsets = [0x768, 0x5560]  # Offset chain to sun value

    # Resolve the final address
    sun_address = get_pointer_address(pm, base_address, offsets)
    
    # Read current sun
    # current_sun = pm.read_int(sun_address)
    # print(f"Current sun: {current_sun}")

    # # Update sun
    # pm.write_int(sun_address, 99999)
    # print("Sun value updated to 99999")

if __name__ == "__main__":
    main()
