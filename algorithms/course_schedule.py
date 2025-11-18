class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # Build adjacency list
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # Track visited states: 0=unvisited, 1=visiting, 2=visited
        state = [0] * numCourses
        
        def has_cycle(course):
            if state[course] == 1:  # Currently visiting = cycle!
                return True
            if state[course] == 2:  # Already visited, no cycle here
                return False
            
            state[course] = 1  # Mark as visiting
            
            # Check all neighbors
            for neighbor in graph[course]:
                if has_cycle(neighbor):
                    return True
            
            state[course] = 2  # Mark as visited
            return False
        
        # Check each course for cycles
        for course in range(numCourses):
            if has_cycle(course):
                return False
        
        return True


if __name__ == "__main__":
    sol = Solution()
    
    numCourses = 2
    prerequisites = [[1, 0]]
    expected = True
    
    result = sol.canFinish(numCourses, prerequisites)
    
    print(f"Input: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print(f"Pass: {result == expected}")