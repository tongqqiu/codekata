__author__ = 'tongqingqiu'

import re, string, timeit


class MySort:

    def sort(self, input):
        """remove all punctuation, and sort"""
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        normal_input = regex.sub('', input.lower())
        array = list(normal_input.replace(' ',''))
        array.sort()
        return ''.join(array)

if __name__ == '__main__':
    mySort = MySort()
    print mySort.sort("When not studying nuclear physics, Bambi likes to play beach volleyball.")

