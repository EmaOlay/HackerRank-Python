def getTotalX(a, b):
    # Write your code here
    x= a+b
    x=sorted(x)
    count=0
    
    for integer in range(1,x[-1]+1):
        cond1=1
        cond2=1
        #first condition
        for i in a:
            if(integer%i!=0):
                cond1=0
        #second condition
        for i in b:
            if(i%integer!=0):
                cond2=0
        if (cond1 and cond2):
            count+=1
    return count