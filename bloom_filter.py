from bitarray import bitarray
import mmh3
 
class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        
    def add(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            self.bit_array[result] = 1
            
    def lookup(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                return False
        return True


if __name__ == '__main__':
    #http://pages.cs.wisc.edu/~cao/papers/summary-cache/node8.html
    # n = 338882, let's set k=8, in order to achieve fP<0.001, m > n*14
    # 10000000 bits = 10Mb
    bf = BloomFilter(10000000, 8)

    lines = open("data/wordlist-utf8.txt").read().splitlines()
    for line in lines:
        bf.add(line)

    print bf.lookup("google")
    print bf.lookup("google1111")