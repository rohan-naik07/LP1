#Number of queens
print ("Enter the number of queens")
N = int(input())

print ("Enter the number of queens
")
N = int(input())

#chessboard
#NxN matrix with all elements 0
board = [[0]*N for _ in range(N)]
col = [0]*N
normal_diagonal = [False] * ((2*N)-1)
reverse_diagonal = [False] * ((2*N)-1)

def is_attack(i, j):
    #checking if there is a queen in row or column
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    #checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def is_attack_bab(i, j):
    #checking if there is a queen in row or column
    return col[j]==True and normal_diagonal[i+j]==True and reverse_diagonal[i-j+(N-1)]==True

def N_queen(n):
    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                #recursion
                #wether we can put the next queen with this arrangment or not
                if N_queen(n-1)==True:
                    return True
                board[i][j] = 0

    return False

def N_queen_bab(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(is_attack_bab(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                col[j]=True
                reverse_diagonal[i-j+(N-1)]=True
                normal_diagonal[i+j]=True

                #recursion
                #wether we can put the next queen with this arrangment or not
                if N_queen(n-1)==True:
                    return True
                board[i][j] = 0
                col[j]=False
                reverse_diagonal[i-j+(N-1)]=False
                normal_diagonal[i+j]=False

    return False

stat = N_queen(N)

if stat == True:
    for i in board:
        print (i)

else:
    print("No result possible")
