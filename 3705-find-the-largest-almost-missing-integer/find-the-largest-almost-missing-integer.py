from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counts = Counter(nums)
        
        # Case 1: Every element is its own subarray
        if k == 1:
            # Find the largest element that appears exactly once overall
            unique_elements = [num for num, count in counts.items() if count == 1]
            return max(unique_elements) if unique_elements else -1
            
        # Case 2: The entire array is the only subarray
        if k == n:
            return max(nums)
            
        # Case 3: 1 < k < n (Only the first or last elements can be valid)
        candidates = []
        if counts[nums[0]] == 1:
            candidates.append(nums[0])
        if counts[nums[-1]] == 1:
            candidates.append(nums[-1])
            
        return max(candidates) if candidates else -1
