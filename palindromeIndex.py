def palindromeIndex(s):
    # Write your code here
    if(s == s[::-1]):
        return -1
    else:
        n=len(s)
        difer=-1
        cont=0
        aux=s
        for i in range(int(n/2)+1):
        #print(s[i],s[n-i-1])
            if (s[i]!=s[n-i-1]):
                aux=aux[::-1].replace(s[n-i-1],'', 1)[::-1]
            #print(aux)
            if(aux==aux[::-1]):
                difer=n-i-1
            else:
                aux=aux+s[n-i-1]
                difer=i
                cont+=1
        if cont>1:
            return -1
        else:
            return difer