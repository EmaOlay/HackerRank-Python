def diagonalDifference(arr):
    # Write your code here
    #la matriz es de n*n
    n=len(arr)
    principal=0
    secundaria=0
    for i in range(n):
        principal+=arr[i][i]
        secundaria+=arr[i][n-1-i]
    return abs(principal-secundaria)


n=3
matriz=[[1,2,3],
        [4,5,6],
        [9,8,9]]
print("Escenario 1:")

res=diagonalDifference(matriz)
print(res)
matriz=[
    [11,2,4],
    [4,5,6],
    [10,8,-12]]
print("Escenario 2:")

res=diagonalDifference(matriz)
print(res)