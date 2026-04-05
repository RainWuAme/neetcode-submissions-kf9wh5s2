class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        ROWS, COLS = len(matrix), len(matrix[0])
        # 建立一個與 Matrix 同大小的 memo 矩陣，初始化為 0
        # memo[r][c] 代表從 (r, c) 出發的最長遞增路徑長度
        memo = [[0] * COLS for _ in range(ROWS)]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            # 如果已經計算過，直接回傳結果 (Memoization 核心)
            if memo[r][c] != 0:
                return memo[r][c]
            
            # 基礎長度為 1 (當前格子自己)
            res = 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # 檢查邊界條件與遞增條件
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    matrix[nr][nc] > matrix[r][c]):
                    # 遞迴計算鄰居，取最大值
                    res = max(res, 1 + dfs(nr, nc))
            
            # 將計算結果存入 memo 供下次直接使用
            memo[r][c] = res
            return res

        max_path = 0
        # 遍歷矩陣中每個點，嘗試作為起點
        for r in range(ROWS):
            for c in range(COLS):
                max_path = max(max_path, dfs(r, c))
                
        return max_path