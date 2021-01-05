class Solution:
    def climbStairs(self, n: int) -> int:
        return sol(n, [None] *( n + 1))


def sol(n, memo):
    if n >=0:
        if memo[n] != None:
            return memo[n]
        if n == 0:
            return 1
        else:
            result = sol(n-1, memo)+sol(n-2,memo)
        memo[n] = result
        return result
    else:
        return 0
