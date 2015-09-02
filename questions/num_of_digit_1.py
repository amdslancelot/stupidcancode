class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        print "\ninput:", n
        result = 0
        r = 1
        while n/r >= 10:
            r *= 10
        while r > 0:
            print "position:", r
            result += (n/r+8)/10*r
            print "1.", (n/r+8)/10*r
            if (n/r-1) % 10 == 0:
                result += n%r+1
                print "2.", n%r+1
            r /= 10
        return result

s = Solution()
s.countDigitOne(120)
s.countDigitOne(1200)
