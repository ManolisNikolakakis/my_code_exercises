class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # Maps number -> its index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i


if __name__ == "__main__":
    sol = Solution()
    
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    
    result = sol.twoSum(nums, target)
    
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print(f"Pass: {result == expected}")