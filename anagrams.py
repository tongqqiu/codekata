__author__ = 'tongqingqiu'

import sys


class Anagrams:
    """A anagram reader class"""

    def __init__(self):
        pass

    @staticmethod
    def read(filename):
        dictionary = {}
        ins = open(filename, "r")
        for line in ins:
            line = line.rstrip()
            array = list(line)
            array.sort()
            sign = ''.join(array)
            if sign in dictionary:
                dictionary[sign] = dictionary[sign] + ' ' + line
            else:
                dictionary[sign] = line
        ins.close()

        for key in dictionary:
            if ' ' in dictionary[key]:
                print dictionary[key]


def main():
    input_file = sys.argv[1]
    Anagrams.read(input_file)


if __name__ == '__main__':
    main()
