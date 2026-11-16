def group_anagrams(strs):
    anagrams = {}

    for word in strs:
        key = ''.join(sorted(word))

        if key not in anagrams:
            anagrams[key] = []

        anagrams[key].append(word)

    return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))
