print("Welcome to tic tac toe!!!!.\n")
m=[]
for p in range(3):
    m.append([])
for p in range(3):
    for q in range(3):
        m[p].append(q)
        m[p][q]='1'
for i in range (3):
    print(m[i])

for k in range (9):
    a=int(input("row number\n"))
    b=int(input("column number\n"))
    if(k%2==0):
        m[a][b]="X"
    else:
        m[a][b]="O"
    for i in range (3):
        print(m[i])
    if(k>2):    
        if(m[0][0]==m[1][1]and m[1][1]==m[2][2]):
            if(m[0][0]!='1' and m[1][1]!='1'):
                if(m[0][0]!='1'):
                    if(k%2==0):
                        p=1
                    else:
                        p=2
                    print("Player %d Wins !!!!\n"%(p))
                    break
        elif(m[0][2]==m[1][1]and m[1][1]==m[2][0]):
            if(m[0][2]!='1' and m[1][1]!='1'):
                if(m[2][0]!='1'):
                    if(k%2==0):
                        p=1
                    else:
                        p=2
                    print("Player %d Wins !!!!\n"%(p))
                    break
        elif(m[0][0]==m[1][0]and m[1][0]==m[2][0]):
            if(m[0][0]!='1' and m[1][0]!='1'):
                if(m[2][0]!='1'):
                    if(k%2==0):
                        p=1
                    else:
                        p=2
                    print("Player %d Wins !!!!\n"%(p))
                    break
        elif(m[0][1]==m[1][1]and m[1][1]==m[2][1]):
            if(m[0][1]!='1' and m[1][1]!='1'):
                if(m[2][1]!='1'):
                    if(k%2==0):
                        p=1
                    else:
                        p=2
                    print("Player %d Wins !!!!\n"%(p))
                    break
        elif(m[0][2]==m[1][2]and m[1][2]==m[2][2]):
            if(m[0][2]!='1' and m[1][2]!='1'):
                if(m[2][2]!='1'):
                    if(k%2==0):
                        p=1
                    else:
                        p=2
                    print("Player %d Wins !!!!\n"%(p))
                    break
        elif(m[0][0]==m[0][1]and m[0][1]==m[0][2]):
            if(m[0][0]!='1' and m[0][1]!='1'):
                if(m[0][2]!='1'):
                    if(k%2==0):
                        p=1
                    else:
                        p=2
                    print("Player %d Wins !!!!\n"%(p))
                    break
        elif(m[1][0]==m[1][1]and m[1][1]==m[1][2]):
            if(m[1][0]!='1' and m[1][1]!='1'):
                if(m[1][2]!='1'):
                    if(k%2==0):
                        p=1
                    else:
                        p=2
                    print("Player %d Wins !!!!\n"%(p))
                    break
        elif(m[2][0]==m[2][1]and m[2][1]==m[2][2]):
            if(m[2][0]!='1' and m[2][1]!='1'):
                if(m[2][2]!='1'):
                    if(k%2==0):
                        p=1
                    else:
                        p=2
                    print("Player %d Wins !!!!\n"%(p))
                    break
print("GAME OVER !!!!")