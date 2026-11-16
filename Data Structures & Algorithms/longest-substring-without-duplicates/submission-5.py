class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 1
        r = 0
        if len(s) == 1:
            return 1
        window = s[r:l]
        for i in range(1, len(s)):
            if len(window) > length:
                length = len(window)
            while (s[i] in window):
                r += 1
                window = s[r:l]
            l += 1
            window = s[r:l]
        if len(window) > length:
                length = len(window)
        return length