def superDigit(n, k):
    # Write your code here
    aux1=[]
    for i in range(len(n)):
        aux1.append(int(n[i]))
    
    for i in range(k):
        aux2=str(sum(aux1))
        aux1=[]
        for i in range(len(aux2)):            
            aux1.append(int(aux2[i]))
    return int(aux2)
    
# Alternative solution
# def superDigit(n, k):
#     # Write your code here
    
#     return (1 + (int(n)*k - 1) % 9)

print(superDigit('9875',4))

print(superDigit('148',3))