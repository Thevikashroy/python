arr = [7,3,8,9,5,12]
ans = -1
n = len(arr)
for i in range(n):
    allXor = 0
    for j in range(n):
        if j != i:
            allXor ^= arr[j]
    if allXor <= arr[i]:
        current = arr[i] - allXor
        if ans == -1:
            ans = current
        if current < ans:
            ans = current
print(ans)