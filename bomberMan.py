def bomberMan(n, grid):
    # Write your code here
    if n==1: #no hago nada
        return grid
    # si n es par lleno la grilla
    if n%2 ==0:
        return ['O'*c for i in range(r)]
    #para los otros casos
    n//=2
    for q in range((n+1) %2 +1): #me aseguro que sean impares
        print(q)
        aux = [['O']*c for i in range(r)]
        xi=[0,0,0,-1,1]
        yi=[0,-1,1,0,0]

        for x in range(r):
            for y in range(c):
                if grid[x][y]== 'O':
                    #lo pongo en '.' y a los adjacentes
                    for i,j in zip(xi,yi):
                        if -1<(x+i)<r and -1<(y+j)<c:
                            aux[x+i][y+j]='.'
        #piso la grilla anterior con aux
        grid=aux

    return["".join(x) for x in grid]








def set(x,y):
    if 0<=x<=r and 0<=y<=c:
        aux[x][y]='.'