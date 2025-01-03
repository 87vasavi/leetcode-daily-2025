class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        l = []
        count = 0
        vowels = ["a", "e", "i", "o", "u"]
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count = count +1
            l.append(count)

        ans = []
        for q in queries:
            i, j = q
            count = l[j]-l[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                count +=1
            ans.append(count)
        return ans

            

