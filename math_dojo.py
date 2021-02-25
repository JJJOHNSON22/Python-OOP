class MathDojo:
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

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).add(2,3).subtract(1,3,4).subtract(1).result
print(x)
# should output 1
