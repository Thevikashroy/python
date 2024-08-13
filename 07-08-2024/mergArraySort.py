
arr1 = [-3,9,15,17,21]
arr2 = [0,1,3,7,9,12,15,18]

i = 0
j = 0
n1 = len(arr1)
n2 = len(arr2)

arr = []
while i<(n1) and j<(n2):
    if arr1[i] < arr2[j]:
        arr.append(arr1[i])
        i += 1
    else:
        arr.append(arr2[j])
        j +=1

while i<len(arr1):
    arr.append(arr1[i])
    i +=1
while j<(n2):
    arr.append(arr2[j])
    j += 1
print(arr)
print(i,j)
        