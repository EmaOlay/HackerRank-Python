def matchingStrings(strings, queries):
    # Write your code here
    res=[0]*(len(queries))
    index=0
    for query in queries:
        for string in strings:
            if string == query:
                res[index]+=1
        index+=1
            
    return res

print("Escenario 1:")
entrada = ['aba','baba','aba','xzxb']
pregunta = ['aba','xzxb','ab']
res = matchingStrings(entrada,pregunta)

print(res)
