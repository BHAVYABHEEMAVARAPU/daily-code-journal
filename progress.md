# DSA Progress Tracker – November 2026

## Daily Progress

| Day | Problem | Topic | Difficulty | Status |
|---|---|---|---|---|
| Day 1 | Contains Duplicate | Arrays & Hashing | Easy | Completed |
| Day 1 | Valid Anagram | Arrays & Hashing | Easy | Completed |
| Day 2 | Two Sum | Arrays & Hashing | Easy | Completed |
| Day 2 | Group Anagrams | Arrays & Hashing | Medium | Completed |
| Day 2 | Top K Frequent Elements | Arrays & Hashing | Medium | Completed |
| Day 3 | Product of Array Except Self | Arrays & Hashing | Medium | Initial Approach Completed |
| Day 4 | Longest Consecutive Sequence | Arrays & Hashing | Medium | Completed |
| Day 5 | Encode and Decode Strings | Arrays & Hashing | Medium | Completed |
| Day 6 | Valid Palindrome | Two Pointers | Easy | Completed |
| Day 6 | Reverse Integer | Math & Geometry | Medium | Completed |
| Day 6 | Missing Number | Arrays & Hashing | Easy | Completed |
| Day 6 | Find X in Sorted Array | Searching | Easy | Completed |

## Statistics

- **Total Problems Practised:** 12
- **Easy:** 6
- **Medium:** 6
- **Hard:** 0
- **Topics Covered:** Arrays & Hashing, Two Pointers, Math & Geometry, Searching

## Key Learnings

### Day 1
- Using sets to identify duplicates.
- Using dictionaries to count character frequencies.
- Comparing frequency dictionaries to validate anagrams.

### Day 2
- Solving Two Sum using nested loops.
- Understanding array indices and pair comparisons.
- Avoiding duplicate pair checks using `j = i + 1`.
- Brute-force time complexity: O(n²).
- Auxiliary space complexity: O(1).
- Using `sorted()` and `join()` to generate common keys for anagrams.
- Using dictionaries to group anagrams.
- Creating nested lists dynamically.
- Understanding `dict.values()` to retrieve grouped results.
- Sorting-based Group Anagrams time complexity: O(n × k log k).
- Using dictionaries for frequency counting.
- Sorting dictionary keys based on their values.
- Understanding `key=freq.get` and `reverse=True`.
- Using list slicing to retrieve the top K elements.
- Top K Frequent Elements time complexity: O(n + m log m).

### Day 3
- Using `math.prod()` to calculate the product of array elements.
- Using `count()` to identify the number of zeros.
- Handling arrays with no zeros, exactly one zero, and multiple zeros.
- Using generator expressions to calculate the product of non-zero elements.
- Understanding how zero affects multiplication.
- Implementing conditional logic for different edge cases.
- Learning that the original problem prohibits division.
- Next step: Solve using prefix and suffix products.

### Day 4 – Longest Consecutive Sequence
- Using sets to remove duplicate elements.
- Understanding average O(1) membership checking.
- Identifying the starting point of a consecutive sequence using `num - 1 not in l`.
- Traversing consecutive numbers using a `while` loop.
- Counting the length of consecutive sequences.
- Using `max()` to maintain the longest sequence.
- Avoiding unnecessary repeated traversal.
- Achieving O(n) average time complexity using a set.

### Day 5 – Encode and Decode Strings
- Designing a custom string encoding format.
- Using length-prefix encoding to preserve string boundaries.
- Using `len()` and string concatenation.
- Understanding delimiters and their role in encoding.
- Using two pointers to traverse an encoded string.
- Finding delimiters using a `while` loop.
- Extracting substrings using string slicing.
- Converting string representations of numbers using `int()`.
- Reconstructing the original list of strings.
- Handling words containing delimiter characters using length information.

### Day 6
- Cleaning strings using `isalnum()` and `lower()`.
- Using `"".join()` with generator expressions.
- Reversing strings using slicing `[::-1]`.
- Checking palindromes through string comparison.
- Extracting digits using the modulo operator `%`.
- Removing digits using integer division `//`.
- Reversing integers mathematically.
- Handling negative numbers using `abs()` and sign restoration.
- Understanding signed 32-bit integer limits and overflow handling.
- Using mathematical formulas to find missing numbers.
- Calculating expected and actual array sums.
- Finding missing values using the difference between two sums.
- Implementing linear search using array indices.
- Returning the index of a matching element.
- Returning `-1` when the target is not found.
- Understanding the difference between linear search O(n) and binary search O(log n).
- Recognizing how sorted arrays can help optimize searching.

## Next Goal

- Continue practising Arrays & Hashing.
- Learn the optimized Two Sum solution using a hash map.
- Explore frequency-counting approaches for Group Anagrams.
- Explore bucket sort for Top K Frequent Elements.
- Solve Product of Array Except Self without division.
- Practice explaining time and space complexity during interviews.
- Learn Binary Search and optimize Find X in Sorted Array.
- Continue with the remaining NeetCode 150 problems.

---

**Current Progress: 12 / 150 Problems**
