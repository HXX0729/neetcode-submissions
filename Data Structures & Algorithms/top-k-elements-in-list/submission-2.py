class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        freq2num = [ [freq, num] for num, freq in freq.items()]
        freq2num.sort(reverse = True)
        return [pair[1] for pair in freq2num[:k]]

        
