class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bitearray = 0


    def hash1(self, str1):
        random_number = 17
        iter_value = 0
        for c in str1:
            code = ord(c)
            iter_value = (iter_value * random_number + code) % self.filter_len
        return iter_value

    def hash2(self, str1):
        random_number = 223
        iter_value = 0
        for c in str1:
            code = ord(c)
            iter_value = (iter_value * random_number + code) % self.filter_len
        return iter_value

    def set_bit(self, index):
        mask = 1 << index
        self.bitearray |= mask
        return index

    def get_bit(self, index):
        mask = 1 << index
        return self.bitearray & mask

    def add(self, str1):
        hash1 = self.hash1(str1)
        hash2 = self.hash2(str1)
        self.set_bit(hash1)
        self.set_bit(hash2)


    def is_value(self, str1):
        hash1 = self.hash1(str1)
        hash2 = self.hash2(str1)
        return self.get_bit(hash1) and self.set_bit(hash2)



