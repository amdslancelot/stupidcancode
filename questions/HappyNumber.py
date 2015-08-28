class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans = []
        while n != 1:
            print n
            n = self.doMath(n)
            print n
            if n in ans:
                return False
            else:
                ans.append(n)
            
        return True

    def doMath(self, n):
        str_n = str(n)
        r = 0
        for e in str_n:
            r += int(e)*int(e)
        
        return r

s = Solution()
print s.isHappy(19)

