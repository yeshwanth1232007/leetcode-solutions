# Problem: Two Sum (Easy)

**Link:** https://leetcode.com/problems/two-sum/

## Approach

I used a dictionary (hash map) to store each number and its index while
iterating through the array. For each number, I calculate its complement
using `target - num` and check whether the complement has already been seen.

This avoids checking every possible pair and makes the solution efficient.

## Complexity

- Time: O(n)
- Space: O(n)

## Notes

An important edge case is when the same number appears twice, such as
`[3, 3]` with target `6`. The dictionary allows the two different indices
to be identified correctly.

The solution returns the indices of the two numbers rather than the
numbers themselves.