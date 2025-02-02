# Time complexity - O(n)
# Space complexity - O(n/2)

# Approach - bfs - Create a hashmap to maintain dependent and independent courses and a queue to keep count
# of dependent courses. Put the independent course with value 0 in the queue. Maintain the count, finally
# return whether count == numCourses 

from queue import Queue
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        q = Queue()
        indegrees = [0 for i in range(numCourses)]
        Map = dict()
        count = 0
        for i in range(len(prerequisites)):
            From = prerequisites[i][1] # independent
            To = prerequisites[i][0] # dependent
            indegrees[To] += 1
            if From not in Map:
                Map[From] = []
            Map[From].append(To)
        

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.put(i)
                count += 1
        
        if count == 0:
            return False
        
        while q.qsize() > 0: #not q.empty():
            curr = q.get()
            if curr in Map:
                edges = Map[curr]
                for edge in edges:
                    indegrees[edge] -= 1
                    if indegrees[edge] == 0:
                        q.put(edge)
                        count += 1
        return count == numCourses