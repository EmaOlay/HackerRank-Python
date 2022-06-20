def dynamicArray(n, queries):
    # Write your code here
    arr=[] 
    l_ans=0
    ans=[]
    for i in range(n):
        arr.append([])
    for i in range(len(queries)):
        idx=((int(queries[i][1])^l_ans)%n)
        # print(f'idx= {idx}')
        # print(f'queries[i][0]={queries[i][0]}')
        if queries[i][0]==1:
            arr[idx].append(int(queries[i][2]))
        elif queries[i][0]==2:
            l_ans=arr[idx][int(queries[i][2])%len(arr[idx])]
            ans.append(l_ans)
            # print(l_ans)
    return ans


dynamicArray(2,'105')