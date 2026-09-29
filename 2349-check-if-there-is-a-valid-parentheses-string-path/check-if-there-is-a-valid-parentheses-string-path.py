class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2:
            return False

        if grid[0][0] == ')':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                val = 1 if grid[i][j] == '(' else -1
                cur = set()

                if i > 0:
                    cur |= dp[i - 1][j]
                if j > 0:
                    cur |= dp[i][j - 1]

                for balance in cur:
                    new_balance = balance + val
                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        return 0 in dp[-1][-1]