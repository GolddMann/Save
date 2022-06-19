from utils import generateHash


class Block:
    def __init__(self, index, prevHash, data):
        self.index = index
        self.hash = generateHash(data)
        self.prevHash = prevHash
        self.data = data

    def __str__(self):
        block = 'Block('
        block += 'index: ' + (str(self.index)) + ', '
        block += 'hash: ' + str(self.hash) + ', '
        block += 'prevHash: ' + str(self.prevHash) + ', '
        block += 'data: ' + str(self.data)
        block += ')'

        return block
