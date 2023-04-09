import struct

def writeToBinaryFile():
    with open('dates.bin', 'wb') as f:
        values = (1.23, True, 'c'.encode())
        packer = struct.Struct('f ? c')
        packer_data = packer.pack(*values)
        f.write(packer_data)

def readFromBinaryFile():
      with open('dates.bin', 'rb') as f:
            file_content = f.read(6)
            print(file_content)
            # values = (file_content)
            packer = struct.Struct('f ? c')
            # packer_data = packer.pack(*values)
            packed_data = packer.unpack(file_content)
            print(packed_data)
            
            # values = (file_content[0], file_content[1], file_content[2].encode())
            # print(values)

            # unpacker = struct.Struct('f ? c')

            # print(unpacker.unpack(file_content))
            # packer = struct.Struct('f ? c')
            # packer_data = packer.pack(*values)
	
readFromBinaryFile()


