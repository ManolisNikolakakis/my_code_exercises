class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        
        start = 0
        max_len = 0
        
        for i in range(len(s)):
            # Odd length palindromes (center is single character)
            len1 = self.expandAroundCenter(s, i, i)
            # Even length palindromes (center is between two characters)
            len2 = self.expandAroundCenter(s, i, i + 1)
            
            current_max = max(len1, len2)
            
            if current_max > max_len:
                max_len = current_max
                start = i - (current_max - 1) // 2
        
        return s[start:start + max_len]
    
    def expandAroundCenter(self, s, left, right):
        # Expand while characters match and in bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Return length (right - left - 1 because we went one step too far)
        return right - left - 1


if __name__ == "__main__":
    sol = Solution()
    
    s = "babad"
    expected = "bab"  # or "aba"
    
    result = sol.longestPalindrome(s)
    
    print(f"Input: s = '{s}'")
    print(f"Output: '{result}'")
    print(f"Expected: '{expected}' (or 'aba')")
    print(f"Valid: {result in ['bab', 'aba']}")