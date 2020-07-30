import random

#Rules
global Place
Place=['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','d1','d2','d3','d4','d5','e1','e2','e3','e4','e5']

global computer_place
computer_place=['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','d1','d2','d3','d4','d5','e1','e2','e3','e4','e5']

def Continue(arr):
    a=[int(i[-1]) for i in arr]
    b=[int(ord(i[0])) for i in arr]
    #print(b)
    if sorted(a)==list(range(min(a),max(a)+1)) and all(j==b[0] for j in b):
        return True
    elif all(j==a[0] for j in a) and sorted(b)==list(range(min(b),max(b)+1)):
        return True
    else:
        return False

def Rule1(arr):
    return all(j==True for j in [Continue(i) for i in arr])

#print(all(j==True for j in [Continue(i) for i in [['a1','a2'],['a2','b2']]]))
#player
global player
player=[['b2','c2','d2'],['b4','c4'],['e4','e5']]

#print(Rule1(player))

#Computer

global computer
computer=[['a3','a4','a5'],['b2','c2'],['e2','e3']]
#print(Rule1(computer))

#Deciding Factor
global result,computer_next_move,user_move,computer_move
result="Null"
computer_next_move=['False']
computer_move=''
user_move=''
global chance
chance="user"


global computer_pre_move

computer_pre_move=[]

def User_Move():
    user=input("Enter Move:")
    if user in Place:
        return user
    else:
        print("Wrong Move!! Enter Valid Move")
        return User_Move()

def Choice():
    return random.choice(Place)

#Final CallBack
def Result():
    global result
    if len(player[0])==0 or all(len(i)==0 for i in player):
        result="\n\nComputer Win.\nMukesh:-Dekha Jitne Diya :)\n\n"
        return True
    elif len(computer[0])==0 or all(len(i)==0 for i in computer):
        result="\n\nUser win"
        return True
    else:
        return False

def User_attack():
    global chance
    res=False
    for i in computer:
        for j in range(len(i)):
            if user_move==i[j]:
                chance="user"
                i.pop(j)
                res=True
                break
    if res is False:
        chance="computer"
        
    return res


def Computer_pre_move():
    global computer_pre_move
    index=Place.index(computer_pre_move[1])
    index1=Place.index(computer_pre_move[2])
    res=int(index1-index)
    if res==5:
        add(Place[index-5])
        add(Place[index+5])
        add(Place[index+1])
        add(Place[index-1])
    




def Computer_attack():
    global chance,computer_pre_move,computer_next_move
    res=False
    for i in player:
        for j in range(len(i)):
            if computer_move==i[j]:
                computer_pre_move.append(i[j])
                computer_next_move[0]="True"
                if len(computer_next_move)==1:
                    Computer_Move()
                if len(computer_pre_move)==3:
                    return 1
                i.pop(j)
                res=True
                break
    if res is False:
        chance="user"
    return res


def add(x):
    if x in computer_place:
        computer_next_move.append(x)
        computer_place.pop(computer_place.index(x))
        
    

def Computer_Move():
    global computer_next_move,computer_move,computer_pre_move
    index=Place.index(computer_move)
    if index>5 and index<19 and index%5!=0 and index%5!=4:
        add(Place[index-5])
        add(Place[index+5])
        add(Place[index+1])
        add(Place[index-1])
    elif index%5==0:
        if index!=20:
            add(Place[index+5])
        add(Place[index+1])
        if index!=0:
            add(Place[index-5])
    elif index%5==4:
        add(Place[index-1])
        if index!=24:
            add(Place[index+5])
        if index!=4:
            add(Place[index-5])
    elif index%5<4:
        add(Place[index+1])
        add(Place[index-1])
        if index<4:
            add(Place[index+5])
        if index>19:
            add(Place[index-5])
    #print(computer_next_move)
    #print(computer_pre_move)
        

def Decide_Move():
    global computer_move,computer_pre_move,computer_next_move
    if computer_next_move[0]=="True":
        computer_move=computer_next_move[random.randint(1,len(computer_next_move)-1)]
        computer_next_move.pop(computer_next_move.index(computer_move))
    else:
        computer_move=Choice()
    if len(computer_next_move)==1:
        computer_next_move[0]='False'
        
    if len(computer_pre_move) in [2,3]:
        computer_pre_move=[]


if Rule1(player):
    while result=="Null":
        if chance=="user":
            user_move=User_Move()
            User_attack()
            if Result():
                print(result)
        elif chance=="computer":
            Decide_Move()
            print("Computer Move:",computer_move)
            Computer_attack()
            if Result():
                print(result)
else:
    print("Not Valid")














    
  
    


