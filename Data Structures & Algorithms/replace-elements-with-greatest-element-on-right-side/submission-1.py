class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max  = -1
        # 2|4|5|3|1|2 -> we will replace last with -1 anyway so we consider the max on the right of last element as -1
        #reverse | new max = max(oldmax, arr[i])

        currMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(currMax, arr[i])
            arr[i] = currMax
            currMax = newMax
        return arr
