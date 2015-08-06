'''
I found there's no good dfs and bfs python version implementation on internet,
so I decided to write one for myself.
'''

graph = {'A': ['B', 'C', 'E'],
         'B': ['D', 'F', 'A'],
         'C': ['G', 'A'],
         'D': ['B'],
         'E': ['F', 'A'],
         'F': ['E', 'B'],
         'G': ['C']}

def dfs1(graph, start):
    visited, stack = [], [start]
    while stack:
        next = stack.pop()
        if next not in visited:
            visited.append(next)
            
            tmp = []
            for e in graph[next]:
                if e not in visited:
                    tmp.append(e)
                    
            for i in range(0, len(tmp)):
                stack.append(tmp.pop()) #put in in reverse order
    return visited

def dfs2(graph, start, visited=None, stack=None):
    if visited is None:
        visited = []
    else:
        if len(visited) == 7:
            return visited
    visited.append(start)

    if stack is None:
        stack = []

    tmp = list(graph[start])
    for i in range(0, len(tmp)):
        e = tmp.pop()
        if e not in visited:
            stack.append(e)

    next = stack.pop()
    return dfs2(graph, next, visited, stack)

def bfs1(graph, start):
    visited, queue = [], [start]
    while queue:
        next = queue.pop(0)
        if next not in visited:
            visited.append(next)
            
            tmp = []
            for e in graph[next]:
                if e not in visited:
                    tmp.append(e)
                    
            for i in range(0,len(tmp)):
                queue.append(tmp.pop(0))
    return visited
    
    
def bfs2(graph, start, visited=None, queue=None):
    if visited is None:
        visited = []
    else:
        if len(visited) == len(graph):
            return visited
    visited.append(start)

    if queue is None:
        queue = []

    tmp = list(graph[start])
    for i in range(0, len(tmp)):
        e = tmp.pop(0)
        if e not in visited:
            queue.append(e)

    next = queue.pop(0)
    return bfs2(graph, next, visited, queue)

print "dfs 1:", dfs1(graph, 'A')
print "dfs 2:", dfs2(graph, 'A')
print "bfs 1:", bfs1(graph, 'A')
print "bfs 2:", bfs2(graph, 'A')
