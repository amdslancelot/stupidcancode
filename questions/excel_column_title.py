import math
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """ 
        r = ""
        expo = int(math.log(n, 26))
        for i in range(expo, 0, -1):
            print "i", i
            times = n/float(26**i)
            print "times", times
            
            isInt = False
            if times >=1 and int(times*100) == int(int(times)*100):
                isInt = True
                
            if isInt:
                times = int(times) - 1
                #n_left = n - int(times)*(26**i)
            else:
                times = int(times)
                #n_left = n - int(times)*(26**i) 
            
            if times >= 1:
                r += chr(int(times)+64)
                n = n - int(times)*(26**i)
            
        r += chr(n+64)
        
        return r
        
s = Solution()
r = s.convertToTitle(701)
#r = s.convertToTitle(1048)
print "ans:", r
