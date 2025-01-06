class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = dict()
        for i in range(len(s)):
            c = s[i]
            if c not in d:
                d[c] = [i]
            elif len(d[c]) == 1:
                d[c].append(i)
            else:
                d[c][1] = i
        
        count = 0
        for c in d:
            if len(d[c])==2:
                m, n  = d[c]
                p = dict()
                for i in range(m+1, n, 1):
                    if s[i] not in p:
                        p[s[i]] = 1
                count = count +len(p)
        return count
            

