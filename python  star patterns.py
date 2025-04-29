#square pattern 10
n=int(input(" enter the  rows:"))
for i in range (n):
    for j in range (n):
         print("*",end=' ')
    print()
#increased triangle 20
n=int (input("enter the rows:"))
for i in range(n):
    for j in range(i+1):
        print("*", end =' ')
    print()
# decreased triangle 24
n=int(input("enter the rows:"))
for i in range(n):
    for j in range(i,n):
        print("*",end = '  ')
    print()
# hill pattern 31 
n=int(input(" enter the rows:"))
for i in range(n):
    for j in range(i,n):
        print(' ',end = ' ')
    for j in range (i):
        print("*", end=' ')
    for j in range(i+1):
        print("*", end= ' ')
    print()
#reverse hill pattern 49
n=int(input("enter the rows:"))
for i in range(n):
    for j   in range(i+1):
        print(' ',end=' ')
    for j in range (i,n-1):
        print("*",end =' ')
    for j in range(i,n):
        print("*",end=' ')
    print()
# diamond pattern 66
#n=int(input("enter the rows:"))
n=31
for i in  range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range (i):
        print('*',end=' ')
    for j in range (i+1):
        print("*",end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end= ' ')
    for j in range(i,n-1):
        print("*",end= ' ')
    for j in range(i,n):
        print("*",end=' ')
    print()
n=4
matrix=[[0]*n for _ in range(n)]
top,bottom,left,right,num=0,n-1,0,n-1,1
while top<=bottom and left<= right:
    for i in range(left,right+1):matrix[top][i]=num;num+=1
    top+=1
    for i in range(top,bottom+1):matrix[i][right]=num;num+=1
    right-=1
    for i in range(right,left-1,-1):matrix[bottom][i]=num;num+=1
    bottom-=1
    for i in range(bottom,top-1,-1):matrix[i][left]=num;num+=1
    left+=1
for row in matrix:
    print(*row)
 
        
    
