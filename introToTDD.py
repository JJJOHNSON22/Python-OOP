import unittest

def reverseList(ulist):
    if len(ulist) % 2 == 0:
        for i in range(0, int(len(ulist) / 2)):
            ulist[i], ulist[len(ulist) - 1 - i] = ulist[len(ulist) - 1 - i], ulist[i]
        return ulist
    else:
        for i in range(0, int(len(ulist))):
            if ulist[i] == ulist[len(ulist) - 1 - i]:
                return ulist
            else:
                ulist[i], ulist[len(ulist) - 1 - i] = ulist[len(ulist) - 1 - i], ulist[i]

def isPalindrome(word):
    for i in range(0, len(word) - 1):
        if word[i] != word[len(word) - i - 1]:
            return False
        elif (i >= len(word) // 2):
            return True
        else:
            i += 1

def coins(change):
    arrCoins = [0,0,0,0]
    # [Quarters, Dimes, Nickels, Pennies]
    while change > 0:
        if change >= 25:
            change -= 25
            arrCoins[0] += 1
        elif change >= 10:
            change -= 10
            arrCoins[1] += 1
        elif change >= 5:
            change -= 5
            arrCoins[2] += 1
        else:
            change -= 1
            arrCoins[3] += 1
    return arrCoins

def factorial(num):
    if num == 1:
        return num
    else:
        return (num * factorial(num - 1))

def fibonacci(num2):
    if num2 <= 1:
        return num2
    else:
        return(fibonacci(num2 - 1) + fibonacci(num2 - 2))
    
    numTerms = 10
    if numTerms <= 0:
        print("Not a positive number.")
    else:
        print("Fibonacci sequence:")
        for i in range(nterms):
            print(fibronacci(i))

print(fibonacci(4))

# class reverseListTest(unittest.TestCase):
#     def testOdd(self):
#         self.assertEqual(reverseList([1,2,3]), [3,2,1])
#     def testNotEqual(self):
#         self.assertNotEqual(reverseList([1,2,3]), [1,2,3])
#     def testNotNone(self):
#         self.assertIsNotNone(reverseList([0,1,2,3]))
#     def testEven(self):
#         self.assertEqual(reverseList([0,1,2,3]), [3,2,1,0])

# class isPalindromeTest(unittest.TestCase):
#     def testEqual(self):
#         self.assertEqual(isPalindrome('gag'), True)
#     def testIsNot(self):
#         self.assertIsNot(isPalindrome('gag'), False)
#     def testTrue(self):
#         self.assertTrue(isPalindrome('gag'))
#     def testFalse(self):
#         self.assertFalse(isPalindrome('gap'))
#     def testIsNotNone(self):
#         self.assertIsNotNone(isPalindrome('dad'))

# class exactChangeTest(unittest.TestCase):
#     def testEqual(self):
#         self.assertEqual(coins(75), [3,0,0,0])
#     def testNotEqual(self):
#         self.assertNotEqual(coins(86), [3,0,2,1])
#     def testOneCoin(self):
#         self.assertEqual(coins(41), [1,1,1,1])
#     def testNotNone(self):
#         self.assertIsNotNone(coins(0), [0,0,0,0])
#     def testBiggerCoins(self):
#         self.assertEqual(coins(5), [0,0,1,0])

# class factorialTest(unittest.TestCase):
#     def testEqual(self):
#         self.assertEqual(factorial(3), 6)
#     def testNotEqual(self):
#         self.assertNotEqual(factorial(4), 4)
#     def testNotNone(self):
#         self.assertIsNotNone(factorial(4))

class fibonacciTest(unittest.TestCase):
    def testEqual(self):
        self.assertEqual(fibonacci(3), 2)
    def testNotEqual(self):
        self.assertNotEqual(fibonacci(2), 2)
    def testNotNone(self):
        self.assertIsNotNone(fibonacci(0))

if __name__ == '__main__':
    unittest.main()

