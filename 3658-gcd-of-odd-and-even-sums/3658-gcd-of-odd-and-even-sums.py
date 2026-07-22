class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = n * n
        even_sum = n * (n + 1)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        return gcd(odd_sum, even_sum)