import struct
import sys

class BinaryFileOpenerAndReader:
    def __init__(self, files):
        self.files = files
        self.first_file = ''
        self.second_file = ''
        self.third_file = ''
        self.fourth_file = ''

    def printDatas(self):
        # 1 feladat
        self.printUnpackedData(self.readFirst())
        self.printUnpackedData(self.readSecond())
        self.printUnpackedData(self.readThird())
        self.printUnpackedData(self.readFourth())

        # 2 feladat
        self.printPackedData(struct.Struct('f ? c'), self.readFirst())
        self.printPackedData(struct.Struct('c 9s i'), self.readSecond())
        self.printPackedData(struct.Struct('i ? f'), self.readThird())
        self.printPackedData(struct.Struct('c f 9s'), self.readFourth())

    def readFirst(self):
        with open(self.files[1], "rb") as f:
            self.first_file = f.read(6)
            packer = struct.Struct('f ? c')
            unpacked_data = packer.unpack(self.first_file)
        return unpacked_data
    
    def readSecond(self):
        with open(self.files[2], "rb") as f:
            self.second_file = f.read(14)
            packer = struct.Struct('c 9s i')
            unpacked_data = packer.unpack(self.second_file)
            return unpacked_data
    
    def readThird(self):
        with open(self.files[3], "rb") as f:
            self.third_file = f.read(10)
            packer = struct.Struct('i ? f')
            unpacked_data = packer.unpack(self.third_file)
            return unpacked_data
    
    def readFourth(self):
        with open(self.files[4], "rb") as f:
            self.fourth_file = f.read(12)
            packer = struct.Struct('c f 9s')
            unpacked_data = packer.unpack(self.fourth_file)
            return unpacked_data
    
    # bináris fájl beolvasása után a pack-elt elemeket printeli ki
    def printUnpackedData(data):
        print(data)

    # az unpack-elt bináris tartalmat printeli ki
    def printPackedData(packer, packed_data):
        print(packer.pack(*packed_data))


binaryFileOpenerAndReader = BinaryFileOpenerAndReader(sys.argv)
binaryFileOpenerAndReader.printDatas()