import struct
# print event.tagPath
# print initialChange
# print newValue


lo = system.tag.read("[default]hr_1_Int").value
hi = system.tag.read("[default]hr_0_Int").value

tup = (lo, hi)

pack_input = struct.pack('>HH', tup[0], tup[1])

display_result = struct.unpack('>f', pack_input)

tagOut = str(display_result)

print tagOut
print type(tagOut)


system.tag.write("[default]reg1Mem.value", tagOut)


def swap(lo, hi):

    tup = (lo, hi)

    pack_input = struct.pack('>HH', tup[0], tup[1])

    display_result = struct.unpack('>f', pack_input)

    return str(display_result)
