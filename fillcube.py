#input and formation of wall matrix
n=int(input())
wall=list()
for i in range(n):
    ele=(input()).split(" ")
    wall.append(ele)
for i in wall:
    for j in range (n):
        if(i[j]=="D"):
            i[j]=int(1)
        if(i[j]=="C"):
            i[j]=int(0)        

#rotate by 90 degrees
def rot90(mat, times):
    for itera in range(times):
        N=n
        for x in range(0, int(N / 2)): 
            for y in range(x, N-x-1):  
                temp = mat[x][y] 
                mat[x][y] = mat[y][N-1-x] 
                mat[y][N-1-x] = mat[N-1-x][N-1-y] 
                mat[N-1-x][N-1-y] = mat[N-1-y][x] 
                mat[N-1-y][x] = temp
    return mat

#melting of blocks function
def melt(wall1):
    for i in range(n):
        c=0
        for j in range(n):
            if(wall1[j][i]==0):
                c+=1
        for j in range(n-1,-1,-1):
            if(j+1>(n-c)):
                wall1[j][i]=0
            else:
                wall1[j][i]=1
    return wall1
            
#find lagest square size
def findsize(M):
    T=[[0 for x in range(len(M[0]))] for y in range(len(M))]
    max=0
    for i in range(len(M)):
        for j in range(len(M[0])):
            T[i][j]=M[i][j]
            if i>0 and j>0 and M[i][j]==1:
                T[i][j]=min(T[i][j-1],T[i-1][j], T[i-1][j-1])+1
            if max<T[i][j]:
                max=T[i][j]
    return max

#action
ans1 = findsize(melt((rot90(wall,1))))
ans2 = findsize(melt((rot90(wall,2))))
ans3 = findsize(melt((rot90(wall,3))))
ans4 = findsize(melt((rot90(wall,4))))

print(max(ans1,ans2,ans3,ans4))