"""
We are given n tasks, T1, ..., Tn
We are also given d dependencies b/w tasks:
- T1 is a prereq of T2
- T1 is a prereq of T3
- T1 is a prereq of T4
- T2 is a prereq of T4
- T4 is a prereq of T5
- T6 is a prereq of T7
- ...

Goal: We would like to batch tasks together so that we can run 
concurrently tasks that fall into the same batch.
- If you assign Ti to batch B, then all of Ti's prereqs must be
assigned to batches 1 through B-1.
- We would like to produce the min amt of batches possible.

Solution:
Batch 1: T1, T6
Batch 2: T2, T3, T7
Batch 3: T4
Batch 4: T5

Algorithm (any language that you feel most familiar with)

tasks = [1, 2, ..., n]
prereqs = [(1, 2), (1, 3), ...]
"""

'''
Build graph:
start - end
1: [2,3]
2: [4]
4: [5,1]
6: [7]

end - start
1: 4
2: 1
3: 1
4: 2
5: 4
7: 6


SOP:
1. Find source: 1,6
2. Start from source, walk through nodes and print:
   level 1: 1,6 (print and add to visited)
   level 2: 2,3,4,7 but 4 needs 2 finishs first, so => 2,3,7 (print and add to visited))
            how to detect 4?
              1. trace back 4 to see if reach [2, 3, 7]
              2. 
   level 3: 4
   level 4: 5
3. 

'''
class Solution():
  def arrangeTasks(self, prereqs):


    self.r = []
    self.m = {}
    self.sources = []
    for req in prereqs:
      start, end = req[0], req[1]
      if start in self.m:
        self.m[start].append(end)
      else:
        self.m[start] = [end]

      '''
      if start not in self.sources:
        self.sources.append(start)
      if end not in self.sources:
        self.sources.append(end)
      '''
    #check cycle
    self.visited = {}
    for k in self.m.keys():
      print "check:", k
      if self.checkCycle(k, self.visited):
        return []

    self.visited = {}
    #find sources
    for n in self.m.keys():
      if self.isStart(n):
        self.sources.append(n)
    print "sources:", self.sources

    for n in self.sources:
      if not self.helper(n, 0):
        return []
    
    return self.r

  def checkCycle(self, n, visited):
    if n in visited and visited[n] == 2:
      return False

    visited[n] = 1
    print "visited", visited
    if n in self.m:
      for end in self.m[n]:
        if end in visited and visited[end] != 2:
          return True
        if end in self.m:
          if self.checkCycle(end, visited):
            return True
    visited[n] = 2
    return False

  def isStart(self, n):
    for vs in self.m.values():
      if n in vs:
          return False
    return True

  def helper(self, n, level):
    self.visited[n] = 1

    if n in self.m:
      for end in self.m[n]:
        if end in self.visited and self.visited[end] == 2:
          continue
        if end in self.visited and self.visited[end] != 2:
          return False
        if not self.helper(end, level+1):
          return False
    
    self.visited[n] = 2
    while level >= len(self.r):
      self.r.append([])
    self.r[level].append(n)
    return True

s = Solution()
print "expected:", [[1, 6], [2, 3, 7], [4], [5]]

prereqs = [[1,2],[1,3],[1,4],[2,4],[2,5],[4,5],[6,7]]
r = s.arrangeTasks(prereqs)
print "input:", prereqs, "\nans:", r
prereqs = [[1,2],[1,3],[1,4],[2,4],[2,5],[4,5],[6,7],[4,2]]
r = s.arrangeTasks(prereqs)
print "input:", prereqs, "\nans:", r
prereqs = [[1,2],[1,3],[2,4],[2,5],[4,5],[6,7],[4,1]]
r = s.arrangeTasks(prereqs)
print "input:", prereqs, "\nans:", r
