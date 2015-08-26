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
        

#a = [6,3,5,9,2,4,1,8,7]
#a = [2,1]
#a = [7,6,5,4,3,2,1]
#a = [1]
a = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
print "origin: %s" % (a)
s = Solution()
print "ans:", s.findKthLargest(a, 2)
