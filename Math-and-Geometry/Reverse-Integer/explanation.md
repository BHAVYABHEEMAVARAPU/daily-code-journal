# Reverse Integer

**Problem:** Given a signed 32-bit integer, reverse its digits. If the reversed integer falls outside the signed 32-bit range, return `0`.

## Approach: Digit Extraction and Reversal

I used mathematical operations to extract each digit and construct the reversed number.

### Step 1: Initialize variables

```python
n = len(str(abs(x)))
l = abs(x)
rev = 0
```

- `abs(x)` removes the negative sign temporarily.
- `n` stores the number of digits.
- `rev` stores the reversed number.

### Step 2: Extract and reverse digits

```python
for i in range(n):
    num = l % 10
    rev = rev * 10 + num
    l = l // 10
```

- `% 10` extracts the last digit.
- `rev * 10 + num` appends that digit to the reversed number.
- `// 10` removes the last digit from the original number.

### Step 3: Restore the sign

```python
if x < 0:
    rev = -rev
```

If the original number was negative, the reversed number is made negative.

### Step 4: Check 32-bit integer overflow

```python
if rev < -(2**31) or rev > 2**31 - 1:
    return 0
```

If the reversed number falls outside the valid signed 32-bit integer range, return `0`.

### Example

**Input:**
```python
x = 123
```

Digit extraction:

- `123 % 10 = 3`
- `12 % 10 = 2`
- `1 % 10 = 1`

Reversed number: `321`

**Output:**
```python
321
```

### Complexity Analysis

Let `d` be the number of digits in the input integer.

- **Time Complexity:** O(d) – Each digit is processed once.
- **Auxiliary Space Complexity:** O(d) for the string created by `str(abs(x))` to calculate the digit count.

### Key Learnings
- Using `abs()` to handle negative numbers.
- Extracting digits using the modulo operator `%`.
- Removing digits using integer division `//`.
- Constructing a reversed integer mathematically.
- Restoring the original sign.
- Handling signed 32-bit integer overflow.
