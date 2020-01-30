# Given a word, return all the anagrams of that word in the English language.


f = open("words.txt", "r")
word_list = f.read().split("\n")
word_list = [w.lower() for w in word_list if len(w) > 0]


anagram_cache = {}
for word in word_list:
    signature = "".join(sorted(word))
    if signature not in anagram_cache:
        anagram_cache[signature] = [word]
    else:
        anagram_cache[signature].append(word)


# Given a word, check each other word in the list and return all that are anagrams
# How do we know if two words are anagrams of each other?

def is_anagram(word1, word2):
    # If length of words are not equal, return false
    if len(word1) != len(word2):
        return False
    letter_list = list(word2)
    for letter in list(word1):
        if letter in letter_list:
            letter_list.remove(letter)
        else:
            return False
    return True


# Time complexity: O(n * w), n is the length of the word list, w is the length of the word
# Time complexity: O(n), n is the length of the word list
# Space complexity: O(1)
def anagrams(word):
    anagrams = []
    for w in word_list:
        if is_anagram(word, w) and w != word:
            anagrams.append(w)
    return anagrams
