from bloom_filter import BloomFilter

__author__ = 'tongqingqiu'

import time

class WordLookup:
    def __init__(self, file_name):
        self.bf = BloomFilter(10000000, 8)
        input_file = open(file_name, "r")
        for file_line in input_file:
            file_line = file_line.rstrip()
            self.bf.add(file_line)
        input_file.close()

    def is_qualified(self, string):
        str_len = len(string)
        if str_len != 6:
            return False
        for i in range(1, str_len - 1):
            first = string[:i]
            second = string[i:]
            if self.bf.lookup(first) and self.bf.lookup(second):
                #print first + '+' + second + '=>' + string
                return True
        return False

def time_code(arg):
    """For running code once,and take time"""
    start = time.clock()
    arg()
    end = time.clock()
    print 'Code time %.6f seconds' % (end - start)

def test():
    word_lookup = WordLookup("data/wordlist-utf8.txt")
    ins = open("data/wordlist-utf8.txt", "r")
    for line in ins:
        line = line.rstrip()
        word_lookup.is_qualified(line)
    ins.close()

if __name__ == '__main__':
    time_code(test)
