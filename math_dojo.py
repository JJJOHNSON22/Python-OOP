import unittest

class mathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        for i in nums:
            self.result += i
        self.result += num
        return self
    def subtract(self, num, *nums):
        for i in nums:
            self.result -= i
        self.result -= num
        return self

class mathDojoTest(unittest.TestCase):
    def setUp(self):
        md = mathDojo()
        self.x1 = md.add(2).add(2,5,1).subtract(3,2).add(2,3).subtract(1,3,4).subtract(1).result
        self.x2 = md.add(2).result
        self.x3 = md.subtract(1).result
    def testEqual(self):
        self.assertEqual(self.x1, 1)
    def testAddition(self):
        self.assertEqual(self.x2, 3)
    def testSubtract(self):
        self.assertIsNotNone(self.x3, 2)

if __name__ == '__main__':
    unittest.main()

# md = mathDojo()
# x = md.add(2).add(2,5,1).subtract(3,2).add(2,3).subtract(1,3,4).subtract(1).result
# print(x)
# should output 1
