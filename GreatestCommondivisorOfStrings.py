class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Find the length of the greatest common divisor
        gcd_length = self.gcd(len(str1), len(str2))
        
        # Check if the substrings of length gcd_length are common divisors
        gcd_str = str1[:gcd_length]
        if self.check_divisor(str1, gcd_str) and self.check_divisor(str2, gcd_str):
            return gcd_str
        
        return ""
    
    # Function to find the greatest common divisor
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    # Function to check if str is a divisor of s
    def check_divisor(self, s: str, str: str) -> bool:
        return s == str * (len(s) // len(str))

        
