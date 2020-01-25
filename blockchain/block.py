import hashlib
import datetime


class Block:
    def __init__(self, previous_hash, data, timestamp):
        self.prevoius_hash = previous_hash
        self.data = data
        self.timestamp = timestamp
        self.nonce = 0
        self.hash = self.hash()

    def hash(self):
        header = "{}{}{}{}".format(self.prevoius_hash, self.data, self.timestamp, self.nonce).encode()

        inner_hash = hashlib.sha256(header).hexdigest().encode()
        self.hash = hashlib.sha256(inner_hash).hexdigest()

        return self.hash

    @staticmethod
    def create_genesis():
        return Block("0", "0", datetime.datetime.now())

    def __str__(self):
        return "hash: {} prev: {} nonce: {}".format(self.hash, self.prevoius_hash, self.nonce)


if __name__ == "__main__":
    genesis_block = Block.create_genesis()

    print("Genesis Block Hash: ", genesis_block.hash)