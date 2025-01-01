class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        zero_count = 0
        one_count = 0

        max_one_count = 0
        for i in range(len(s)):
            if s[i]=='1':
                max_one_count +=1

        ans = 0

        for i in range(len(s)-1):
            if s[i]=='0':
                zero_count +=1
            if s[i]=='1':
                one_count +=1
            ans = max(ans, max_one_count-one_count+zero_count)
        

        return ans

        
