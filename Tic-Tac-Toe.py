from random import *
mat=[[9,9,9],[9,9,9],[9,9,9]]


player1=0
player2=0
check=0
lab=0
for row in mat:
    print("\t",row)
print(""" The object of Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as 1 and the second is O.
Players alternate placing Xs and Os on the game board until either oppent has three in a row or all nine squares are filled. 1 always goes first, and in the event that no one has three in a row, the stalemate is called a cat game.""")
while(player1!=1 or player2!=1):
    if(lab!=1):
        m,n=input("Player 1, enter the order\n").split(" ")
        #print(m,n)
        m=int(m)
        n=int(n)
        check=0
        if(m>2 and n>2):
            continue
    
        if(m<3 and n<3):
            if(mat[m][n]!=1 and mat[m][n]!=0):
                mat[m][n]=1
            else:
                #print("test")
                for row in mat:
                    for i in row:
                       # print(i)
                        if(i==9):
                            check=0
                            break
                        else:
                            check=1
                if(check==1):
                    break
                else:
                    continue
        if(m==0 and n ==0):
            #print("Player 1,1st condition")
            if(mat[m+1][n]==1 and mat[m+2][n]==1):
                player1=1
                break
            if(mat[m][n+1]==1 and mat[m][n+2]==1):
                player1=1
                break
            if(mat[m+1][n+1]==1 and mat[m+2][n+2]==1):
                player1==1
                break
            for row in mat:
                print("\t",row)
           
        if(m==1 and n==0):
            #print("Player 1,2nd condition")
            if(mat[m-1][n]==1 and mat[m+1][n]==1):
                player1=1
                break
            if(mat[m][n+1]==1 and mat[m][n+2]==1):
                player1=1
                break
            for row in mat:
                print("\t",row)
           
        if(m==2 and n==0):
            #print("Player 1,3rd condition")
            if(mat[m-1][n]==1 and mat[m-2][n]==1):
                player1=1
                break
            if(mat[m][n+1]==1 and mat[m][n+2]==1):
                player1=1
                break
            if(mat[m-1][n+1]==1 and mat[m-2][n+2]==1):
                player1=1
                break
            for row in mat:
                print("\t",row)
            
        if(m==0 and n==1):
            #print("Player 1,4th condition")
            if(mat[m][n-1]==1 and mat[m][n+1]==1):
                player1=1
                break
            if(mat[m+1][n]==1 and mat[m+2][n]==1):
                player1=1
                break
            for row in mat:
                print("\t",row)
            
        if(m==0 and n==2):
            #print("Player 1,5th condition")
            if(mat[m][n-1]==1 and mat[m][n-1]==1):
                player1=1
                break
            if(mat[m+1][n]==1 and mat[m+2][n]==1):
                player1=1
                break
            if(mat[m+1][n-1]==1 and mat[m+2][n-2]==1):
                player1=1
                break
            for row in mat:
                print("\t",row)
            
        if(m==1 and n==2):
            #print("Player 1,6th condition")
            if(mat[m-1][n]==1 and mat[m+1][n]==1):
                player1=1
                break
            if(mat[m][n-1]==1 and mat[m][n-2]==1):
                player1=1
                break
            for row in mat:
                print("\t",row)
            
        if(m==2 and n==2):
            #print("Player 1,7th condition")
            if(mat[m-1][n]==1 and mat[m-2][n]==1):
                player1=1
                break
            if(mat[m][n-1]==1 and mat[m][n-2]==1):
                player1=1
                break
            if(mat[m-1][n-1]==1 and mat[m-2][n-2]==1):
                player1=1
                break
            for row in mat:
                print("\t",row)
            
        if(m==2 and n==1):
            #print("Player 1,8th condition")
            if(mat[m][n-1]==1 and mat[m][n+1]==1):
                player1=1
                break
            if(mat[m-1][n]==1 and mat[m-2][n]==1):
                player1=1
                break
            for row in mat:
                print("\t",row)
            
        if(m==1 and n==1):
            #print("Player 1,9th condition")
            if(mat[m][n-1]==1 and mat[m][n+1]==1):
                player1=1
                break
            if(mat[m-1][n]==1 and mat[m+1][n]==1):
                player1=1
                break
            if(mat[m-1][n-1]==1 and mat[m+1][n+1]==1):
                player1=1
                break
            if(mat[m-1][n+1]==1 and mat[m+1][n-1]==1):
                player1=1
                break
            for row in mat:
                print("\t",row)
    p,q=input("Player 2,enter the order\n").split(" ")
    p=int(p)
    q=int(q)
    if(p>2 and q>2):
        continue
    if(p<3 and q<3):
        if(mat[p][q]!=1 and mat[p][q]!=0):
            mat[p][q]=0
            lab=0
        else:
           # print("test2")
            for row in mat:
                for i in row:
                    #print(i)
                    if(i==9):
                        check=0
                        break;
                    else:
                        check=1
            if(check==1):
                break
            else:
                lab=1
                continue 
            
        if(p==0 and q ==0):
            #print("1st condition")
            if(mat[p+1][q]==0 and mat[p+2][q]==0):
                player2=1
                break
            if(mat[p][q+1]==0 and mat[p][q+2]==0):
                player2=1
                break
            if(mat[p+1][q+1]==0 and mat[p+2][q+2]==0):
                player2==1
                break
            for row in mat:
                print("\t",row)
           
        if(p==1 and q==0):
            #print("2nd condition")
            if(mat[p-1][q]==0 and mat[p+1][q]==0):
                player2=1
                break
            if(mat[p][q+1]==0 and mat[p][q+2]==0):
                player2=1
                break
            for row in mat:
                print("\t",row)
           
        if(p==2 and q==0):
            #print("3rd condition")
            if(mat[p-1][q]==0 and mat[p-2][q]==0):
                player2=1
                break
            if(mat[p][q+1]==0 and mat[p][q+2]==0):
                player2=1
                break
            if(mat[p-1][q+1]==0 and mat[p-2][q+2]==0):
                player2=1
                break
            for row in mat:
                print("\t",row)
            
        if(p==0 and q==1):
            #print("4th condition")
            if(mat[p][q-1]==0 and mat[p][q+1]==0):
                player2=1
                break
            if(mat[p+1][q]==0 and mat[p+2][q]==0):
                player2=1
                break
            for row in mat:
                print("\t",row)
            
        if(p==0 and q==2):
            #print("5th condition")
            if(mat[p][q-1]==0 and mat[p][q-1]==0):
                player2=1
                break
            if(mat[p+1][q]==0 and mat[p+2][q]==0):
                player2=1
                break
            if(mat[p+1][q-1]==0 and mat[p+2][q-2]==0):
                player2=1
                break
            for row in mat:
                print("\t",row)
            
        if(p==1 and q==2):
            #print("6th condition")
            if(mat[p-1][q]==0 and mat[p+1][q]==0):
                player2=1
                break
            if(mat[p][q-1]==0 and mat[p][q-2]==0):
                player2=1
                break
            for row in mat:
                print("\t",row)
            
        if(p==2 and q==2):
            #print("7th condition")
            if(mat[p-1][q]==0 and mat[p-2][q]==0):
                player2=1
                break
            if(mat[p][q-1]==0 and mat[p][q-2]==0):
                player2=1
                break
            if(mat[p-1][q-1]==0 and mat[p-2][q-2]==0):
                player2=1
                break
            for row in mat:
                print("\t",row)
            
        if(p==2 and q==1):
            #print("8th condition")
            if(mat[p][q-1]==0 and mat[p][q+1]==0):
                player2=1
                break
            if(mat[p-1][q]==0 and mat[p-2][q]==0):
                player2=1
                break
            for row in mat:
                print("\t",row)
            
        if(p==1 and q==1):
            #print("9th condition")
            if(mat[p][q-1]==0 and mat[p][q+1]==0):
                player2=1
                break
            if(mat[p-1][q]==0 and mat[p+1][q]==0):
                player2=1
                break
            if(mat[p-1][q-1]==0 and mat[p+1][q+1]==0):
                player2=1
                break
            if(mat[p-1][q+1]==0 and mat[p+1][q-1]==0):
                player2=1
                break
            for row in mat:
                print("\t",row)
                
        
                
                
       
if(check==1):
    print("MATCH DRAW")
    exit
if(player2==1):
    print("Player 2 won")
    for row in mat:
        print("\t",row)
if(player1==1):
    print("Player 1 won")
    for row in mat:
        print("\t",row)
    
