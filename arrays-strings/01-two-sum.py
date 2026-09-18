class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []


# ==========================================
# LOCAL TESTING
# ==========================================

solution = Solution()


# Test Case 1 - Typical case
nums = [2, 7, 11, 15]
target = 9

result = solution.twoSum(nums, target)

print("Test Case 1")
print("Input:", nums)
print("Target:", target)
print("Output:", result)
print("Expected:", [0, 1])
print()


# Test Case 2 - Edge case: duplicate values
nums = [3, 3]
target = 6

result = solution.twoSum(nums, target)

print("Test Case 2")
print("Input:", nums)
print("Target:", target)
print("Output:", result)
print("Expected:", [0, 1])