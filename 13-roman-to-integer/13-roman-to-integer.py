class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {'I':1,
              'V':5,
              'X':10,
              'L':50,
              'C':100,
              'D':500,
              'M':1000}
        s = list(s)
        i = 0
        result = 0
        addit = 0
        while (i<len(s)):
            if s[i] in [j for j in sym]:
                if i != len(s)-1:
                    if sym[s[i]] < sym[s[i+1]]:
                        addit = sym[s[i+1]] - sym[s[i]]
                        i += 1
                    else:
                        addit = sym[s[i]]
                else:
                    if sym[s[i]] > sym[s[i-1]]:
                        addit = sym[s[i]] - sym[s[i-1]]
                        i += 1
                    else:
                        addit = sym[s[i]]
            i += 1
            print(addit)
            result = result + addit
        return result