










# using dp approch this problem
def fnw(n,dp):
    if n <=3:
        dp[n] = n
        return n
    
    if dp[n] != 0:
        return dp[n]
    
    ans1 = fnw(n-1,dp)
    dp[n-1] = ans1

    ans2 = fnw(n-2,dp)
    dp[n-2] =  ans2

    return ans1+ans2
    
    # return fnw(n-1)+fnw(n-2)






def main():
    n = 10
    dp = [0 for i in range(n+1)]
    ans = fnw(n,dp)
    print(ans)
main()