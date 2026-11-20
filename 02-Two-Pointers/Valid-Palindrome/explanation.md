# Valid Palindrome

**Problem:** Given a string, determine whether it is a palindrome after converting uppercase letters to lowercase and removing all non-alphanumeric characters.

## Approach: String Cleaning and Reversal

I used Python string methods and slicing to check whether the given string is a palindrome.

### Step 1: Clean the string

```python
ct = "".join(char.lower() for char in s if char.isalnum())
```

- `isalnum()` checks whether a character is a letter or digit.
- `lower()` converts uppercase characters into lowercase.
- `"".join()` combines the filtered characters into a new string.

### Step 2: Reverse and compare

```python
if ct == ct[::-1]:
    return True
else:
    return False
```

- `[::-1]` reverses the string.
- If the cleaned string and its reverse are equal, it is a palindrome.

### Example

**Input:**
```python
s = "A man, a plan, a canal: Panama"
```

**Cleaned string:**
```text
amanaplanacanalpanama
```

**Output:**
```python
True
```

### Complexity Analysis

Let `n` be the length of the input string.

- **Time Complexity:** O(n) – Cleaning and reversing the string take linear time.
- **Space Complexity:** O(n) – A cleaned string and its reversed copy are created.

### Key Learnings
- Using `isalnum()` to filter characters.
- Using `lower()` for case normalization.
- Using `"".join()` with a generator expression.
- Reversing strings using slicing.
- Comparing strings to identify palindromes.
