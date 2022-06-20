def balancedSums(arr):
    tot = sum(arr)
    #lo que me va quedando a la izq
    add = 0
    for i in arr:
        if add == tot-i-add:
            return "YES"
        add+=i
    return "NO"

entrada = [1,2,3]
print(balancedSums(entrada))

entrada = [1,2,3,3]
print(balancedSums(entrada))

entrada = [1]
print(balancedSums(entrada))

entrada = [1,2]
print(balancedSums(entrada))

entrada = [1,4,1]
print(balancedSums(entrada))

entrada = [1,1,4,1,1]
print(balancedSums(entrada))
entrada = [2,0,0,0]
print(balancedSums(entrada))

entrada = [0,0,2,0]
print(balancedSums(entrada))