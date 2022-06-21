def anagram(s):
    # Write your code here
    n=len(s)
    if n%2 !=0 :
        return -1
    else:
        count=0
        mid=int(n/2)
        s1=s[:mid]
        s2=s[mid:]
        for i in s1[:]:
            if(i not in s2[:]):
                count+=1
        return count