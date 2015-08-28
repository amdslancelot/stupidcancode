class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSort(nums, 0, len(nums)-1, k)

    def quickSort(self, a, start, end, k):
        adjusted_k = (len(a) - 1 - (k-1))

        print "start", start, "end", end
        if start == end:
            if start == adjusted_k:
                print "return:", a[adjusted_k]
                return a[adjusted_k]
            else:
                return None
        elif start > end:
            return None
        
        pivot = end
        wall = start
        for i in range(start, end):
            print "wall", wall, "i", i
            if a[pivot] > a[i]:
                if i != wall:
                    t = a[wall]
                    a[wall] = a[i]
                    a[i] = t
                wall = wall + 1
        
        if a[pivot] < a[wall]:
            t = a[wall]
            a[wall] = a[pivot]
            a[pivot] = t

        print "a:", a, "k:", k, "wall:", wall

        if wall == adjusted_k:
            print "return:", a[adjusted_k]
            return a[adjusted_k]
        else:
            ans1 = self.quickSort(a, start, wall-1, k)
            if ans1 is not None:
                return ans1
            else:
                return self.quickSort(a, wall+1, end, k) 
#nums = [99,99]
nums = [6,8,1,3,7,9,5,2,4]
print "origin: %s" % (nums)
s = Solution()
r = s.findKthLargest(nums, 1)
print r
