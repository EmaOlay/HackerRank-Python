def maxMin(k, arr):
    arr.sort()
    n=len(arr)
    result = arr[k-1] - arr[0]
    for i in range(n-k+1):
        if arr[i+k-1] - arr[i] < result:
            result = arr[i+k-1] - arr[i]
    return result


entrada=[1,4,7,2]

print(maxMin(2,entrada))

entrada=[100,200,300,350,400,401,402]

print(maxMin(3,entrada))