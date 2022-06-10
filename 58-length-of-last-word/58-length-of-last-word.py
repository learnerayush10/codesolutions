class Solution:
    def lengthOfLastWord(self, s: str):
        s = s.rstrip()
        return len(s[s.rfind(" ") + 1 : None])
