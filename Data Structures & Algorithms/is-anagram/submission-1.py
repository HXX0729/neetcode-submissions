class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        for ch in s:
            dict_s[ch] += 1
        for ch in t:
            dict_t[ch] += 1
        return dict_s == dict_t