class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        
        di = {i: letter for i, letter in enumerate(string.ascii_lowercase, start=0)}
        dl = {letter: i for i, letter in enumerate(string.ascii_lowercase, start=0)}
        diff_l = list(0 for i in range(len(s)))

        for i in range(len(shifts)):
            u, v, d = shifts[i]
            if d==0:
                d =-1
            diff_l[u] += d
            if v+1<len(s):
                diff_l[v+1] += -d
        
        for i in range(1, len(diff_l)):
            diff_l[i] += diff_l[i-1]
        
        ans = ""
        for i in range(len(s)):
            idx = (dl[s[i]]+diff_l[i])%26
            ans = ans+di[idx]

        return ans
