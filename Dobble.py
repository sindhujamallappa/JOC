"""
8 objects in each card(definate number of objects)
Pick any 2 cards only 1 object is common (exactly 1 symbol in column)
deck of 50 cards
.....................................
2 lists
definate num of alphabets in each list
Having exact 1 alphabets in common
"""
import string
import random
symbols=[]
symbols=list(string.ascii_letters)
#print(string.ascii_letters) #consiss of both upper and lowers case letters
card1=[0]*5
card2=[0]*5 #having only 5 alphabets
pos1=random.randint(0,4)
pos2=random.randint(0,4) 
print(pos1)
print(pos2)
#pos1 and pos2 are same alphabet positions in card1 and card2
samesymbol=random.choice(symbols)
symbols.remove(samesymbol)
if(pos1==pos2):
    card2[pos1]=samesymbol
    card1[pos2]=samesymbol
else: #not equal
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
while(i<5): #other alphabets 
    if(i!=pos1 and i!=pos2):
        alphabet1=random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2=random.choice(symbols)
        symbols.remove(alphabet2) 
        card1[i]=alphabet1
        card2[i]=alphabet2
    i=i+1
print (card1)
print (card2)

ch=input("Spot the similar symbol")
if ch==samesymbol:
    print("Correct")
else:
    print("Wrong")