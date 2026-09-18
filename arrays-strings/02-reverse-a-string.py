class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# ==========================================
# LOCAL TESTING
# ==========================================

solution = Solution()

# Test Case 1 - Typical case
s = ["h", "e", "l", "l", "o"]

solution.reverseString(s)

print("Test Case 1")
print("Output:", s)
print("Expected:", ["o", "l", "l", "e", "h"])
print()


# Test Case 2 - Edge case: single character
s = ["a"]

solution.reverseString(s)

print("Test Case 2")
print("Output:", s)
print("Expected:", ["a"])