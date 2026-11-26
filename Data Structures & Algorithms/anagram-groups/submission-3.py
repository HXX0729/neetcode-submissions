class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            key = str(sorted(list(s)))
            d[key].append(s)
  

        return [v for v in d.values()]


