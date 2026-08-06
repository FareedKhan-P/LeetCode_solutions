class Solution:
    def int_to_digit(self, a):
        arr = [int(x) for x in str(a)]
        return arr
    def smallestNumber(self, n: int, t: int) -> int:
        arr = [int(x) for x in str(n)]
        result = 1
        for x in arr:
            result = result * x
        if result % t == 0:
            return n
        while True:
            n += 1
            arr = self.int_to_digit(n)
            result = 1
            for x in arr:
                result = result * x
            if result % t == 0:
                return n
            