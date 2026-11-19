# Encode and Decode Strings

**Problem:** Design an algorithm to encode a list of strings into a single string and decode the encoded string back into the original list.

## Approach: Length-Prefix Encoding

I used a length-prefix encoding technique to combine multiple strings into one string while preserving enough information to reconstruct the original strings.

### 1. Encoding

For each word:
- Calculate its length using `len()`.
- Convert the length into a string.
- Append `#` as a delimiter.
- Append the original word.

Example:

Input:
```python
["hello", "world"]
```

Encoded output:
```text
5#hello5#world
```

### 2. Decoding

I used two pointers, `i` and `j`, to identify the length and extract each word.

1. Start scanning from index `i`.
2. Move `j` until the delimiter `#` is found.
3. Convert the characters before `#` into an integer to get the word length.
4. Calculate the starting and ending positions of the word.
5. Extract the word using string slicing.
6. Move `i` to the end of the extracted word and repeat.

### Example

Encoded string:
```text
5#hello5#world
```

Decoding process:

- Read `5` before `#`.
- Extract the next 5 characters: `hello`.
- Move to the next encoded section.
- Read `5` before `#`.
- Extract the next 5 characters: `world`.

Output:
```python
["hello", "world"]
```

### Complexity Analysis

Let N represent the total number of characters across all input strings and k represent the number of strings.

- **Encoding:** O(N + k) time.
- **Decoding:** O(N) time.
- **Space Complexity:** O(N) for the encoded or decoded output.

### Key Learnings

- Designing a custom string encoding format.
- Using string concatenation and `len()`.
- Understanding delimiters and length-prefix encoding.
- Using two pointers to traverse strings.
- Extracting substrings using slicing.
- Reconstructing original data without ambiguity, even when words contain the delimiter character.

### Important Observation

Using the length of each word instead of relying only on a delimiter makes the encoding robust when the original words themselves contain `#` characters.
