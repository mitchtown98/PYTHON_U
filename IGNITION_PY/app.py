import struct


def swap(lo, hi):

    tup = (lo, hi)

    print(hex(tup[0]))

    print(hex(tup[1]))

    valPack = struct.pack('>HH', tup[0], tup[1])

    print(valPack)

    display = struct.unpack('>f', valPack)

    print(display)


swap(16988, 2621)
