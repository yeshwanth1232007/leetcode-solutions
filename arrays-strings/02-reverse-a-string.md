# Problem: Reverse a String (Easy)

**Link:** https://leetcode.com/problems/reverse-string/

## Approach

I used the two-pointer technique. One pointer starts from the beginning
of the string and another starts from the end. I swap the characters at
both positions and move the pointers toward the center until the string
is completely reversed.

## Complexity

- Time: O(n)
- Space: O(1)

## Notes

The string is modified in-place, as required by the problem.

I also tested a single-character string as an edge case. Since there is
only one character, no swapping is necessary.