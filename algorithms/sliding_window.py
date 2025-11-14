from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        result = []
        dq = deque()
        for i in range(len(nums)):
            while dq and dq[0] < i - k + 1: # remove indices out of bound
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]: # remove indices that are smaller
                dq.pop()
            dq.append(i)
            if i >= k - 1: # start when we have full window
                result.append(nums[dq[0]])
        
        return result


if __name__ == "__main__":
    sol = Solution()
    
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    expected = [3, 3, 5, 5, 6, 7]
    result = sol.maxSlidingWindow(nums, k)
    
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print(f"Pass: {result == expected}")