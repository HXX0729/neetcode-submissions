class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        greatest = 1
        s = set(nums)
        for ele in s:
            if ele - 1 not in s:
                length = 1
                while (ele + 1 ) in s:
                    length += 1
                    greatest = max(greatest, length)
                    ele += 1
        return greatest