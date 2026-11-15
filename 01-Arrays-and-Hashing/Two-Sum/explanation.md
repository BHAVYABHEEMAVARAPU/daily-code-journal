# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays & Hashing  
**Approach:** Brute Force

## Problem
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to the target.

## Approach
1. Use an outer loop to select the first element.
2. Use an inner loop starting from `i + 1` to select the second element.
3. Check whether their sum equals the target.
4. If it does, return their indices.
5. If no pair is found, return an empty list.

## Dry Run

Input: `nums = [1, 3, 5, 5]`, `target = 10`

| i | j | Sum | Result |
|---|---|---|---|
| 0 | 1 | 1 + 3 = 4 | Continue |
| 0 | 2 | 1 + 5 = 6 | Continue |
| 0 | 3 | 1 + 5 = 6 | Continue |
| 1 | 2 | 3 + 5 = 8 | Continue |
| 1 | 3 | 3 + 5 = 8 | Continue |
| 2 | 3 | 5 + 5 = 10 | Found! |

Output: `[2, 3]`

## Complexity Analysis
- **Time Complexity:** O(n²) – Nested loops check pairs of elements.
- **Space Complexity:** O(1) – No additional data structures are used.

## Key Learnings
- Nested loops
- Array indexing
- Avoiding duplicate pair checks using `j = i + 1`
- Returning indices instead of values

## Optimization
This brute-force approach can be optimized to O(n) time using a hash map. I will implement that as a separate solution later.
