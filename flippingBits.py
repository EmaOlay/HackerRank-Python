def flippingBits(n):
    # Write your code here
    #lo niego y lo paso a complemento a1
    aux=~n+(1 << 32)
    return aux

print("Escenario 1:")
entrada=3
res=flippingBits(entrada)
print(res)

print("Escenario 2:")
entrada=2147483647
res=flippingBits(entrada)
print(res)

print("Escenario 2:")
entrada=1
res=flippingBits(entrada)
print(res)