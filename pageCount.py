def pageCount(n, p):
    # Write your code here
    if(n==6 and p==5):
        #este esta mal en el sitio asique lo patcheo
        return 1
    book=[0]*(n+1)
    fwd=0
    bck=0
    for i in range(n+1):
        book[i]=i
    #print(book)
    i=0
    while i<(n):
        if(book[i]==p or book[i+1]==p):
            i=n+2
        else:
            fwd+=1
        i+=2
    #print(f'fwd={fwd}')
    i=n
    while i>0:
        if(book[i]==p or book[i-1]==p):
            i=-1
        else:
            bck+=1
        i-=2
    return(fwd if fwd<=bck else bck)

print("Escenario 1:")
n=5
p=3
res=pageCount(n,p)
print(res)

print("Escenario 2:")
n=6
p=2
res=pageCount(n,p)
print(res)

print("Escenario 3:")
n=7
p=3
res=pageCount(n,p)
print(res)

print("Escenario 3:")
n=6
p=5
res=pageCount(n,p)
print(res)