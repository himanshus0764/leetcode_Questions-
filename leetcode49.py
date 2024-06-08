from collections import defaultdict

# Input list
a = ["eat", "tea", "tan", "ate", "nat", "bat"]

matching_bucket = []
non_matching_bucket = []
non_matching_dict = defaultdict(list)

# Reference word for character matching (can be any word as per the initial idea, here it's kept simple for anagram grouping)
reference_word = a[0]

# Iterate through each word in the list
for w in a:
    char_set = tuple(sorted(w))
    non_matching_dict[char_set].append(w)

# Separate words into matching and non-matching buckets based on their group size
for char_set, words in non_matching_dict.items():
    if len(words) > 1:
        matching_bucket.extend(words)  # Add all words to matching_bucket if there are multiple anagrams
    else:
        non_matching_bucket.extend(words)  # Otherwise, add to non_matching_bucket

print("Matching Bucket:", matching_bucket)
print("Non-matching Bucket:", non_matching_bucket)
