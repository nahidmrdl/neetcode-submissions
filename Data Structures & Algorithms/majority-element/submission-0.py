class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        majority_element, majority_count = 0, 0
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            if freq[n] > majority_count:
                majority_element = n
                majority_count = freq[n]

        return majority_element
