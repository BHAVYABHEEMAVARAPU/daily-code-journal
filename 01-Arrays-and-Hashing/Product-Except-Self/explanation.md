# Product of Array Except Self

**Problem:** Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements of `nums` except `nums[i]`.

## Approach: Total Product and Zero Handling

I solved this problem by calculating the total product of the array and handling different cases depending on the number of zeros.

### Step 1: Calculate the required values

- `mul = math.prod(nums)` – Calculates the product of all elements.
- `z = nums.count(0)` – Counts the number of zeros.
- `res = math.prod(x for x in nums if x != 0)` – Calculates the product of all non-zero elements.

### Step 2: Handle three cases

**Case 1: No zeros (`z == 0`)**

Since there are no zeros, the product except the current element can be calculated by dividing the total product by that element.

`answer[i] = mul // nums[i]`

**Case 2: More than one zero (`z > 1`)**

Every product except one element will still contain at least one zero.

Therefore, every element in the result is `0`.

**Case 3: Exactly one zero (`z == 1`)**

- If the current element is zero, the answer is the product of all non-zero elements.
- If the current element is non-zero, the answer is zero because the product still contains the zero.

### Example

**Input:**
`nums = [1, 2, 3, 4]`

Total product = 24

| Element excluded | Product |
|---|---:|
| 1 | 24 |
| 2 | 12 |
| 3 | 8 |
| 4 | 6 |

**Output:**
`[24, 12, 8, 6]`

### Complexity Analysis

Let `n` be the number of elements in the array.

- **Time Complexity:** O(n) – Product calculation, zero counting, and iteration each take linear time.
- **Auxiliary Space Complexity:** O(1) – Excluding the output list, only a constant amount of additional space is used.
- **Output Space:** O(n) – To store the resulting array.

### Important Note

This is my initial solution using division and explicit zero handling. It produces the required result for valid integer inputs, but it does not satisfy the original problem's constraint of solving it without division.

**Key Learning:** Understanding how zero affects multiplication and breaking a problem into different cases before implementing the solution.
