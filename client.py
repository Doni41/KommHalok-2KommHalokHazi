import struct
import sys

class BinaryFileOpenerAndReader:
    def __init__(self, files):
        self.files = files

    def printDatas(self):
        # 1 feladat
        self.printAsBinaryData(self.readFirst(), struct.Struct('f ? c'))
        self.printAsBinaryData(self.readSecond(), struct.Struct('c 9s i'))
        self.printAsBinaryData(self.readThird(), struct.Struct('i ? f'))
        self.printAsBinaryData(self.readFourth(), struct.Struct('c f 9s'))

        # 2 feladat
        self.printBinaryFileData(self.readFirst())
        self.printBinaryFileData(self.readSecond())
        self.printBinaryFileData(self.readThird())
        self.printBinaryFileData(self.readFourth())

    def readFirst(self):
        with open(self.files[1], "rb") as f:
            file_content = f.read(6)
            values = [file_content[0], file_content[1], file_content[2].encode()]
            packer = struct.Struct('f ? c')
            packer_data = packer.pack(*values)
        return packer_data
    
    def readSecond(self):
        with open(self.files[2], "rb") as f:
            file_content = f.read(14)
            values = [file_content[0].encode(), file_content[1:10].encode(), file_content[10]]
            packer = struct.Struct('c 9s i')
            packer_data = packer.pack(*values)
            return packer_data
    
    def readThird(self):
        with open(self.files[3], "rb") as f:
            file_content = f.read(10)
            values = [file_content[0], file_content[1], file_content[2]]
            packer = struct.Struct('i ? f')
            packer_data = packer.pack(*values)
            return packer_data
    
    def readFourth(self):
        with open(self.files[4], "rb") as f:
            file_content = f.read(12)
            values = [file_content[0].encode(), file_content[1], file_content[2:].encode()]
            packer = struct.Struct('c f 9s')
            packer_data = packer.pack(*values)
            return packer_data
    
    # bináris fájl beolvasása után a pack-elt elemeket printeli ki
    def printBinaryFileData(data):
        print(data)

    # az unpack-elt bináris tartalmat printeli ki
    def printAsBinaryData(binary_data, unpacker):
        print(unpacker.unpack(binary_data))

    # csak tesztelesre hasznalom ezt a fuggvenyt 
    def testing(self):
        with open('test.txt', 'rb') as f:
            file_content = f.read()
            # values = [file_content[0], file_content[1], file_content[2].encode()]
            print(file_content)
            values = (12.3, 1, 'd'.encode())
            print(values)
            packer = struct.Struct('f ? 1s')
            packer_data = packer.pack(*values)
            print(packer_data)


binaryFileOpenerAndReader = BinaryFileOpenerAndReader(sys.argv)
# binaryFileOpenerAndReader.printDatas()