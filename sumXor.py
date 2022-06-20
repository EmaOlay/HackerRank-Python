def sumXor(n):
    # Esta solucion es muy didactica pero lenta
    count=0
    for i in range(n+1):
        #print("{0:b}".format(n+i),"{0:b}".format(n^i))
        if((n+i)==(n^i)):
            count+=1
    return(count)

#Esta solucion hace uso de los conceptos de carry y overflow
#Es complicada de visualizar pero es muy rapida
def sumXor(n):
    return(1 if n == 0 else 1 << (bin(n)[2:].count('0')))
# Con aux los resultados son identicos pero 
# pedir memoria lleva tiempo
print("1:")
print(sumXor(5))
print("2:")
print(sumXor(10))
print("3:")
print(sumXor(0))
print("4:")
print(sumXor(111113456))
print("5:")
print(sumXor(1111111113456))
