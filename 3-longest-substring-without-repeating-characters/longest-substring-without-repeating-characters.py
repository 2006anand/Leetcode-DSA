class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  
        
        left = 0
        max_length = 0

        for right in range(len(s)):
            ch = s[right]
            if ch in char_index and char_index[ch] >= left:
                left = char_index[ch] + 1

            char_index[ch] = right
            max_length = max(max_length, right - left + 1)

        return max_length