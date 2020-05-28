def tictactoe():
    checkSol=['*','#','*']
    matrix=['a','b','c','d','e','f','g','h','i']
    matrix1=[['a','b','c'],['d','e','f'],['g','h','i']]
    mapping=[[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]


    while(True):
        user1=''
        user2=''
        update(matrix1,checkSol)
    
        user1=str(input("\nUser (x) Turn :"))
        for k in matrix:
            loc=matrix.index(str(user1))

        #print("Loc:",loc)
        loc1=mapping[loc]
        #print(loc1)
        u1=loc1[0]
        u2=loc1[1]
        #print(u1,u2)
        matrix1[int(u2)][int(u1)]='X'
        update(matrix1,checkSol)
           
        user2=input("\nUser (O) Turn :")
        for k in matrix:
            loc=matrix.index(str(user2))
        loc1=mapping[loc]
        #print(loc1)
        u1=loc1[0]
        u2=loc1[1]
        #print(u1,u2)
        matrix1[int(u2)][int(u1)]='O'
        update(matrix1,checkSol)

def update(matrix1,checkSol):
    print("*************************\n")
    for i in range(len(matrix1)):
            for j in range(len(matrix1)):
                print(matrix1[i][j]," ",end='')
            print()

    # Checking Diagonal 1
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            if(i==j):
                checkSol[j]=matrix1[i][j]
                
    if(checkSol[0] == checkSol[1] == checkSol[2]):
        if(checkSol[0]=='X'):
            print("Player X Won ....!")
            exit()
        elif(checkSol[0]=='O'):
            print("Player O Won ....!")
            exit()
    
    
    checkSol[0]='*'
    checkSol[1]='#'
    checkSol[2]='*'
    m=0
    n=2
     # Checking Diagonal 2
    for i in range(0,len(matrix1)):
        checkSol[i]=matrix1[m][n]
        m=m+1
        n=n-1
        
    if(checkSol[0] == checkSol[1] == checkSol[2]):
        if(checkSol[0]=='X'):
            print("Player X Won ....!")
            exit()
        elif(checkSol[0]=='O'):
            print("Player O Won ....!")
            exit()
    
    
    checkSol[0]='*'
    checkSol[1]='#'
    checkSol[2]='*'
    # Checking rows 
    for i in range(0,len(matrix1)):
        for j in range(0,len(matrix1)):
            #print("Ctr:",ctr1)
            #print("CheckSol[ctr]=",checkSol[ctr1])
            #print(matrix1[i][j],"*(*(")
            checkSol[j]=matrix1[i][j]
            
        if(checkSol[0] == checkSol[1] == checkSol[2]):
            if(checkSol[0]=='X'):
                print("Player X Won ....!")
                exit()
            elif(checkSol[0]=='O'):
                print("Player O Won ....!")
                exit()
        else:
            checkSol[0]='*'
            checkSol[1]='#'
            checkSol[2]='*'

    checkSol[0]='*'
    checkSol[1]='#'
    checkSol[2]='*'
    # Checking columns 
    for i in range(0,len(matrix1)):
        for j in range(0,len(matrix1)):
            #print("Ctr:",ctr1)
            #print("CheckSol[ctr]=",checkSol[ctr1])
            #print(matrix1[i][j],"*(*(")
            checkSol[j]=matrix1[j][i]
            
        if(checkSol[0] == checkSol[1] == checkSol[2]):
            if(checkSol[0]=='X'):
                print("Player X Won ....!")
                return()
            elif(checkSol[0]=='O'):
                print("Player O Won ....!")
                return()
        else:
            
            checkSol[0]='*'
            checkSol[1]='#'
            checkSol[2]='*'
    
    checkDraw=0
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            if(matrix1[i][j]=='X' or matrix1[i][j]=='O'):
                checkDraw=checkDraw+1

    if(checkDraw==9):
        print("Game Draw ....!")
        return()


tictactoe()
