def caesarCipher(s, k):
    # Write your code here
    #creo alfabeto
    while k>=26:
        k-=26

    ini=ord('a')
    list1 = list(s)
    alfabet=[]
    Alfabet=[]
    for i in range(ini,ini+26):
        alfabet.append(chr(i))
    ini=ord('A')
    for i in range(ini,ini+26):
        Alfabet.append(chr(i))
    for i in range(len(s)):
        if(ord(s[i])>=ord('A') and ord(s[i])<=ord('Z')):
            if (ord(s[i])-ord('A')+k)<(ord('Z')-ord('A')):  
                list1[i]=Alfabet[ord(s[i])-ord('A')+k]
            else:
                list1[i]=Alfabet[ord(s[i])-ord('A')+k-(ord('Z')-ord('A'))-1]

        if(ord(s[i])>=ord('a') and ord(s[i])<=ord('z')):
            if (ord(s[i])-ord('a')+k)<ord('z')-ord('a'):  
                list1[i]=alfabet[ord(s[i])-ord('a')+k]
            else:
                list1[i]=alfabet[ord(s[i])-ord('a')+k-(ord('z')-ord('a'))-1]
    
    s=''.join(list1)
    return(s)

entrada='middle-Outz'
caesarCipher(entrada,2)

entrada='1X7T4VrCs23k4vv08D6yQ3S19G4rVP188M9ahuxB6j1tMGZs1m10ey7eUj62WV2exLT4C83zl7Q80M'

print(caesarCipher(entrada,27))