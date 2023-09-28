import struct

values=(1,b'ab',2.7)
packer = struct.Struct('i 2s f') #Int , char[2], float
#The previous line shows the format of the sent data
packed_data = packer.pack(*values)
print(packed_data)

unpacker = struct.Struct('i 2s f')
unpacked_data= packer.unpack(packed_data)
print(unpacked_data)

print(struct.calcsize('i 2s f'))

print(packer.size)

