#Rules for the game, 3 entities Rock, Paper, Scissors
def rock_paper_scissors(num1, num2, bit1, bit2):
    p1=int(num1[bit1])%3 #p1 place holder at bit position bit1 in num1 and %3 coz v want answer in 0,1,2
    p2=int(num2[bit1])%3
    if(player_one[p1]==player_two[p2]):
        print("Draw")#Draw is not printing
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        print("Player 1 wins")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Paper"):
        print("Player 2 wins")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Scissor"):
        print("Player 2 wins")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Rock"):
        print("Player 1 wins")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Rock"):
        print("Player 2 wins")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Paper"):
        print("Player 1 wins")
#dictionry
player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={0:'Paper',1:'Rock',3:'Scissor'}
#user input the number and the secret bit position in the number
while(1): #1-True
    num1=input("Player 1 enter your choice")
    num2=input("Player 2 enter your choice")
    bit1=int(input("Player 1 enter the secret bit position"))
    bit2=int(input("Player 2 enter the secret bit position"))
    rock_paper_scissors(num1, num2, bit1, bit2)
#default input type in python is string so need to convert i into integer
#restrich or terminate the while loop
    ch=input("Do you want to continue? Y?N")
    if (ch=='n'):
        break

