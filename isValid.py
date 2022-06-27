'''
Sherlock considers a string to be valid if all characters of the string appear the same number of times.
It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times.
Given a string , determine if it is valid.
If so, return YES, otherwise return NO.
'''

def isValid(s):
    #los caracteres solo seran minus
    #list de apariciones de cada letra
    frec= [0]*(ord('z')-ord('a')+1)
    #itero el string
    for letra in s:
        frec[(ord(letra)-ord('a'))]+=1
    
    for i in range(len(frec)-1,0,-1):
        if frec[i]==0:
            frec.pop(i)
    #print(frec)
    if frec[:-1]==frec[0:]:
        return 'YES'
    else:
        for i in range(len(frec)):
            aux=frec[:]
            aux[i]-=1
            if(aux[i]==0):
                aux.pop(i)
            #print(aux[::-1],aux[::])
            if aux[::-1]==aux[:]:
                return 'YES'
    #print(frec)
    return 'NO'
    

string ='aabbcd'
print(isValid(string))

string = 'aabc'
print(isValid(string))

string = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
print(isValid(string))

string = 'dassafnaspfjnspjndfaspfjnsapdjfnsapifneunasddfjnasdfjnsadfjnasdfjnfuenfsadjnfasdjfnsadfnuenfsajdnfsajdfnsuefnsdfjnsadfjnsafdujnsufenrfsdfjnsalkdjfnsaeufnsdfunsdfjnsadfjnsafdusneufneufuenfeunfuenfenfuenfuefuefuefuenfuenfuenfuefuefnuefnuenfeufnuefuefuenfneufneufneufnsjdfnsjdfnskdfjnsdjfnsdfjknsdjfnskjdfnskjdfnskjdfnskjdfnaslodfnawiuenasdlkjafnsalkdjfneunsadkjfneukfnsauefneufneufnusandfusanfduenfuenfsdljfnasldkjfnuwieunf'
print(isValid(string))

string = 'zzzaaaz'
print(isValid(string))