class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 1:
            return [s]
        
        map = {}
        new_s = '' #the original string removed odd char and half the length
        num_of_odd_char = 0
        self.odd_char = '' #record the only odd num char
        
        for e in s:
            if e in map:
                map[e] += 1
            else:
                map[e] = 1
        
        for k,v in map.items():
            if v == 1:
                num_of_odd_char += 1
                self.odd_char = k #found odd char
            else:
                if v%2 != 0:
                    num_of_odd_char += 1
                    self.odd_char = k #found odd char
                    
                for i in xrange(v/2):
                    new_s += k
            
        if num_of_odd_char > 1:
            return [] #exception
            
        self.r = []
        self.dp = {}
        self.helper("", new_s)
        return self.r
        
    def helper(self, prefix, s):
        if prefix in self.dp:
            return
        
        if len(s) == 0:
            self.r.append(prefix + self.odd_char + prefix[::-1]) # add odd char & mirror the other half
            return
        
        self.dp[prefix] = 1
        for i in xrange(len(s)):
            self.helper(prefix+s[i], s[:i]+s[i+1:])
        
s = Solution()
r = s.generatePalindromes("aab")
print "ans", r
