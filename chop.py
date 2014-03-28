__author__ = 'tongqingqiu'

import unittest

class Chopper:
    """A simple example class"""
    def chop(self,target, array):
        low = 0
        high = len(array)-1
        while low <= high:
            mid = (low + high)/2
            value = array[mid]
            if value > target:
                high = mid -1
            elif value < target:
                low = mid + 1
            else:
                return mid
        return -1




class TestSequenceFunctions(unittest.TestCase):
    def test_binary_search(self):
        chopper = Chopper()
        self.assertEqual(-1,chopper.chop(1,[]))

        self.assertEqual(-1,chopper.chop(3,[1]))
        self.assertEqual(0,chopper.chop(1,[1]))

        self.assertEqual(0,chopper.chop(1,[1,3,5]))
        self.assertEqual(1,chopper.chop(3,[1,3,5]))
        self.assertEqual(2,chopper.chop(5,[1,3,5]))
        self.assertEqual(-1,chopper.chop(2,[1,3,5]))
        self.assertEqual(-1,chopper.chop(4,[1,3,5]))
        self.assertEqual(-1,chopper.chop(6,[1,3,5]))

        self.assertEqual(0,chopper.chop(1,[1,3,5,7]))
        self.assertEqual(-1, chopper.chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, chopper.chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, chopper.chop(8, [1, 3, 5, 7]))