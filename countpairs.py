def PairsCount(arr, n, sum):
 
    count = 0  
 
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count
 
 
arr = [-4, 4, 7, -1, 2]
n = len(arr)
sum = 3
print("Count of pairs is",
      PairsCount(arr, n, sum))