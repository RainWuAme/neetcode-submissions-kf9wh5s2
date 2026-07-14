class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        def dfs(crs):
            if preMap[crs] == []:
                return True
            if crs in visiting:
                return False

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True