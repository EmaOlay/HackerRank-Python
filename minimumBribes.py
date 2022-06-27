def minimumBribes(q):
    #se le resta 1 a cada elemento para que value coincida con el indice
    #Entonces el enumarate
    q = [i-1 for i in q]
    bribes = 0
    
    for i, value in enumerate(q):
        cur = i 
        if value - cur > 2:
            print("Too chaotic")
            return
        for k in q[max(value - 1, 0):i]:
            if k > value:
                bribes += 1

    print(bribes)
    

q=[2,1,5,3,4]
minimumBribes(q)