def pangrams(s):
    aux=s.lower()
    # Write your code here
    num_leters=ord('z')+1-ord('a')
    count=[0]*num_leters 
    for i in range(len(aux)):
        if aux[i]!=' ':
            #print(ord(aux[i])-97)
            count[ord(aux[i])-97]+=1
    for algo in count:
        if algo ==0:
            return 'not pangram'
    return 'pangram'

print("Escenario 1:")
entrada = 'We promptly judged antique ivory buckles for the next prize'

res=pangrams(entrada)
print(res)

print("Escenario 2:")
entrada = 'We promptly judged antique ivory buckles for the prize'
res=pangrams(entrada)
print(res)

