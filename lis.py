def lis(a):
    dp = [0] * (len(a) + 1)
    if len(a) == 0:
        return 0
    dp[0] = 1
    for i in range(1, len(a)):
        max_seen_so_far = -5
        for j in range(i-1, -1, -1):
            if a[j] < a[i]:
                if max_seen_so_far < dp[j] + 1:
                    max_seen_so_far = dp[j] + 1
        dp[i] = max_seen_so_far
    return max(dp)
print lis([1, 2, 3, 5, 2, 7])
