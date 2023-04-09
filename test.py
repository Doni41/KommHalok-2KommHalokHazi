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
            packer = struct.Struct('f ? c')
            packed_data = packer.unpack(file_content)
            print(packed_data)
            print(packer.pack(*packed_data))


def writeToBinaryFile2():
    with open('dates2.bin', 'wb') as f:
        values = ('a'.encode(), '123456789'.encode(), 235)
        packer = struct.Struct('c 9s i')
        packer_data = packer.pack(*values)
        f.write(packer_data)


def readFromBinaryFile2():
      with open('dates2.bin', 'rb') as f:
            file_content = f.read(16)
            print(file_content)
            packer = struct.Struct('c 9s i')
            packed_data = packer.unpack(file_content)
            print(packed_data)
            print(packer.pack(*packed_data))

def writeToBinaryFile3():
    with open('dates3.bin', 'wb') as f:
        values = (124, False, 44.56)
        packer = struct.Struct('i ? f')
        packer_data = packer.pack(*values)
        f.write(packer_data)


def readFromBinaryFile3():
      with open('dates3.bin', 'rb') as f:
            file_content = f.read(12)
            print(file_content)
            packer = struct.Struct('i ? f')
            packed_data = packer.unpack(file_content)
            print(packed_data)
            print(packer.pack(*packed_data))


def writeToBinaryFile4():
    with open('dates4.bin', 'wb') as f:
        values = ('f'.encode(), 55.123, '987654321'.encode())
        packer = struct.Struct('c f 9s')
        packer_data = packer.pack(*values)
        f.write(packer_data)


def readFromBinaryFile4():
      with open('dates4.bin', 'rb') as f:
            file_content = f.read(17)
            print(file_content)
            packer = struct.Struct('c f 9s')
            packed_data = packer.unpack(file_content)
            print(packed_data)
            print(packer.pack(*packed_data))
	
# writeToBinaryFile4()
readFromBinaryFile4()


