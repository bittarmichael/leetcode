from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = defaultdict(int)
        hashmap_t = defaultdict(int)

        for letter in s:
            if letter not in hashmap_s:
                hashmap_s[letter] += 1
            else:
                hashmap_s[letter] += 1

        for letter in t:
            if letter not in hashmap_t:
                hashmap_t[letter] += 1
            else:
                hashmap_t[letter] += 1
            
        if hashmap_s == hashmap_t:
            return True
        return False
