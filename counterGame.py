def counterGame(n):
    # Write your code here
    cont=0
    while n>1:
        if(n and (not(n & (n - 1))) ):
            n=int(n/2)
        else:
            i=1
            while i <n:
                i=i*2
            n=int(n-i/2)
        cont+=1
    if (cont%2==0):
        return "Richard"
    else:
        return "Louise"

print(counterGame(6))