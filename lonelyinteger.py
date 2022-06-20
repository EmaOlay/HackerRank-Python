

def lonelyinteger(a):
    # Write your code here
    res=0
    match=False
    for i in range(len(a)):
        match=False
        for j in range(len(a)):
            print('a[i]=',a[i],'a[j]=',a[j])
            if a[i]==a[j] and i!=j:
                match=True
        if not(match):
            return a[i]


print("Escenario 1:")
entrada=[1,2,3,4,3,2,1]

res=lonelyinteger(entrada)
print(res)

print("Escenario 2:")
entrada=[1,1,2]

res=lonelyinteger(entrada)
print(res)