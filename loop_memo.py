class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        i = 2
        while i<=n:
            dp[i] = dp[i - 2] + dp[i -1]
            i = i + 1
        return dp[n]
            
