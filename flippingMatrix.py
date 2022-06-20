def flippingMatrix(a):
    n=int(len(a[0])/2)
    suma=0
    for i in range(n):
        for j in range(n):
            suma += max(max(a[i][j],a[2*n-i-1][j]),max(a[i][2*n-j-1],a[2*n-i-1][2*n-j-1]))
    return(suma)