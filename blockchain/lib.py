from blockchain.block import Block
import datetime


class Blockchain:
    def __init__(self, genesis_block, chain=[]):
        self.chain = chain
        self.chain.append(genesis_block)

        self.difficulty = 4

    def add(self, block):
        self.chain.append(block)

    def mine(self, block):
        while True:
            if block.hash[:self.difficulty] == "0" * self.difficulty:
                self.add(block)
                break
            else:
                block.nonce += 1





if __name__ == "__main__":
    genesis_block = Block.create_genesis()

    blockchain = Blockchain(genesis_block)

    database = ['Mike', 'Angela', 'Jade', 'Michael']

    for data in database:
        block = Block(blockchain.chain[-1].hash, data, datetime.datetime.now())
        blockchain.mine(block)

    for block in blockchain.chain:
        print(block)
