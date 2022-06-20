def birthday(s, d, m):
    # Write your code here
    res=0
    max=len(s)-m+1
    for i in range(0,max if max>0 else 1):
        if sum(s[i:i+m])==d:
            res+=1
    return res

print('Primer escenario:')
s=[2,2,1,3,2]
d=4
m=2

res=birthday(s,d,m)
print(res)

print('Segundo escenario:')
s=[4]
d=4
m=1

res=birthday(s,d,m)
print(res)

print('tercer escenario:')
s=[2,3,4,4,2,1,2,5,3,4,4,3,4,1,3,5,4,5,3,1,1,5,4,3,5,3,5,3,4,4,2,4,5,2,3,2,5,3,4,2,4,3,3,4,3,5,2,5,1,3,1,4,2,2,4,3,3,3,3,4,1,1,4,3,1,5,2,5,1,3,5,4,3,3,1,5,3,3,3,4,5,2]
d=26
m=8

res=birthday(s,d,m)
print(res)