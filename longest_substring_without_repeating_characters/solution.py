class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0
        result = 0
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[i])
            result = max(result, i-left+1)
        return result

s = Solution()