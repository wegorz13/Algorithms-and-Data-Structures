#F(x,y)=min( F(x-1,y)+A[x][y],F(x,y-1)+A[x][y])
def chessboard_rec(A):
    N=len(A)
    DP=[[float('inf')]*N for i in range(N)]
    DP[0][0]=0
    for i in range(1,N):
        DP[i][0]=A[i][0]
        DP[0][i]=A[0][i]
    def F(i,j,N):
        if i-1>=0  and DP[i-1][j]!=float('inf'):
            DP[i-1][j]= F(i-1,j,N)
        if  j-1>=0 and DP[i][j-1]!=float('inf'):
            DP[i][j-1]=F(i,j-1,N)
        return min(A[i][j] +DP[i-1][j],A[i][j] +DP[i][j-1])
    return F(N-1,N-1,N)

def las(c):
	n = len(c)
	val = [0 for _ in range(n)]
	val[0] = c[0]
	val[1] = max(c[0], c[1])
	for i in range(2, n):
		val[i] = max(c[i]+val[i-2], val[i-1])
	return val[n-1]

arr=[1,2,3,4,1]

arr.remove(arr[0])

print(arr)