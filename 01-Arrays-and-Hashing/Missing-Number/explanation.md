# Missing Number

**Problem:** Given an array containing `n` distinct numbers from the range `[0, n]`, find the one number that is missing.

## Approach: Mathematical Sum Formula

I used the sum formula to calculate the expected total and compared it with the actual sum of the array.

### Step 1: Calculate the expected sum

```python
tot = (n * (n + 1)) // 2
```

This calculates the sum of all numbers from `0` to `n`.

### Step 2: Calculate the actual sum

```python
add = 0

for num in nums:
    add += num
```

I iterate through the array and calculate the sum of the existing elements.

### Step 3: Find the missing number

```python
return tot - add
```

The difference between the expected sum and the actual sum gives the missing number.

### Example

**Input:**
```python
nums = [3, 0, 1]
```

- Expected sum = 3 × 4 / 2 = 6
- Actual sum = 3 + 0 + 1 = 4
- Missing number = 6 - 4 = 2

**Output:** `2`

### Complexity Analysis

- **Time Complexity:** O(n) – One traversal of the array.
- **Auxiliary Space Complexity:** O(1) – Only a constant number of variables are used.

### Key Learnings
- Applying mathematical formulas to array problems.
- Calculating the expected sum.
- Finding missing values using the difference between two sums.
- Using a single traversal to calculate the actual sum.
