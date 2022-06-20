def gridChallenge(grid):
    # Write your code here
    new_grid=[]
    n=len(grid)
    col=len(grid[0])
    for i in range(n):
        new_grid.append(sorted(grid[i]))
        # print(new_grid[i])
    for i in range(col):
        aux = [sub[i] for sub in new_grid]
        if (aux != sorted(aux)):
            return 'NO'
    return 'YES'
    

grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']

print(gridChallenge(grid))

grid = ['abc','lmp','qrt']
print(gridChallenge(grid))

grid=['mpxz','abcd','wlmf']
print(gridChallenge(grid))

grid=['eibjbwsp','ptfxehaq','jxipvfga','rkefiyub','kalwfhfj','lktajiaq','srdgoros','nflvjznh']
print(gridChallenge(grid))