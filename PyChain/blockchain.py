from block import Block


class BlockChain:
    def __init__(self):
        self.blocks = []

    def push(self, block):
        self.blocks.append(block)

    def __repr__(self):
        string = ""
        for block in self.blocks:
            string += str(block) + "\n"
        return string

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    block = Block(0, 0, 0)
    blockchain = BlockChain()
    blockchain.push(block)
    print(blockchain)
