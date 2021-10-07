import unittest
from tripletsZero import TripletsZero

class TestTriplets(unittest.TestCase):
    t = TripletsZero()
    def testTrueTriplets(self):
        self.assertEqual(self.t.checkTripletsZero([-1, 0, 1]), 0, "Equal")
        self.assertEqual(self.t.checkTripletsZero([-4, 1, 3]), 0)
        self.assertEqual(self.t.checkTripletsZero([5, -2, -3]), 0)
        self.assertEqual(self.t.checkTripletsZero([-10, 7, 3]), 0)

    def testFalseTriplets(self):
        self.assertNotEqual(self.t.checkTripletsZero([-1, 0, -1]), 0)
        self.assertNotEqual(self.t.checkTripletsZero([1, 1, -1]), 0)
        self.assertNotEqual(self.t.checkTripletsZero([-1, 5, -1]), 0)
        self.assertNotEqual(self.t.checkTripletsZero([7, 4, 5]), 0)

    def testRemoveDuplicates(self):
        self.assertEqual(len(self.t.removeDuplicates([[1,0,-1], [1,0,-1]])), 1)
        self.assertEqual(len(self.t.removeDuplicates([[1, 0, -1], [1, 0, -1], [1,1,1]])), 2)
        self.assertEqual(len(self.t.removeDuplicates([[1, 0, -1], [1, 0, -1], [1, 1, 1],[1,2,3]])), 3)
        self.assertEqual(len(self.t.removeDuplicates([[1, 0, -1], [1, 0, -1], [1, 1, 1], [1, 2, 3], [1,1,1]])), 3)

if __name__ == '__main__':
    unittest.main()

