class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Two pointer approach for remaining two numbers
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result


if __name__ == "__main__":
    sol = Solution()
    
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    
    result = sol.threeSum(nums)
    
    print(f"Input: nums = {nums}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
