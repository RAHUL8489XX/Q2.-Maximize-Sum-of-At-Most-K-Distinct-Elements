class Solution:
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Get distinct elements
        unique_nums = list(set(nums))
        
        # Step 2: Sort in descending order
        unique_nums.sort(reverse=True)
        
        # Step 3: Pick top k elements
        return unique_nums[:k]
©leetcode
