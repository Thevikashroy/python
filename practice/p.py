arr1 = [1,2,3,4,5]
arr2 = [1,2,3]
# z = arr1.union(arr2)
# print(z)
# # n = len(z)
# # for i in range(1,n):
# #     print(i)
z = set(arr1+arr2)
# n = len(z)
# count =0
# for i in range(n-1,-1,-1):
#     count += 1
# print(count)
# arr leader
# arr = [16,17,4,3,5,40]
# # output(17,5,2)
# # maxi = float["-inf"]
# n = len(arr)
# ans = []
# max = float("-inf")
# for i in range(n-1,-1,-1):
#     if arr[i] >= max:
#         ans.append(arr[i])
#         max = arr[i]
#         rev = ans[::-1]
# print(ans)
        

# # for i in range(len(arr)):
# #     if arr[i] >= maxi:
# #         maxi = arr[i]
# #         ans.append(maxi)
# #     reversed = ans[::-1]

# # print(rev)



# a = "abc"
# print(a*3)




# Input: 
arr1 = [1, 2, 4, 6, 10]
arr2 = [4, 5, 6, 9, 12]


arr3 = arr1 + arr2
arr3.sort()
print(arr3)



# low = 0
# mid = 0
# high = len(arr3)
# if high % 2 == 0:
#     mid = (low+high) // 2 
#     res = (arr3[mid] + arr3[mid - 1])
# print(res)




# i = 0
# j = 0
# n1 = len(arr1)
# n2 = len(arr2)

# arr = []
# while i<(n1) and j<(n2):
#     if arr1[i] < arr2[j]:
#         arr.append(arr1[i])
#         i += 1
#     else:
#         arr.append(arr2[j])
#         j +=1

# while i<len(arr1):
#     arr.append(arr1[i])
#     i +=1
# while j<(n2):
#     arr.append(arr2[j])
#     j += 1
# print(arr)



        