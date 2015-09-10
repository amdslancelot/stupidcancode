class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        print "\ninput:", n
        result = 0
        r = 1
        # Get 
        while n/r >= 10:
            r *= 10
            
        while r > 0:
            print "position:        ", r

            # See how many "times" the current digit passed 2
            # If so, num = "times" * "current 10's level"
            passed2 = (n/r+8)/10
            if passed2 > 0: 
                result += passed2*r
            print "collect method 1:", passed2*r, "added!"

            # If current digit == 1,
            # count the num of "remains" to decide how many 1s to add
            if (n/r) % 10 == 1:
                remains = n%r
                result += remains+1 # +1 for 10
                print "collect method 2:", remains+1, "added!"
            r /= 10
        return result

s = Solution()
print s.countDigitOne(13), "VS 6", 
print s.countDigitOne(19), "VS 12"
print s.countDigitOne(111)
print s.countDigitOne(113), "VS 40"
print s.countDigitOne(120), "VS 53"
print s.countDigitOne(222), "VS 153"
print s.countDigitOne(1200), "VS 641"
