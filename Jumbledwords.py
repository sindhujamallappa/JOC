import random

def choose():
    words=['ranbow', 'computer', 'science', 'mathematics', 'player', 'condition', 'revers', 'water', 'board']
    pick=random.choice(words)
    return pick

def jumble(word):
    join(random.samp(word, len(word)))#choose all the letters in the word i random order


def play():
    p1name=input("Player 1, Enter your name")
    p2name=input("Player 2, Enter your name")
    pp1=0 #player 1 score
    pp2 = 0 #player 2 score
    turn = 0 #Alternative turns
    while(1):
        #computer giving words
        picked_word=choose()
        #computer creating a question
        qn = jumble(picked_word)
        print(qn)
        #Alternate the turns
        if turn%2 ==0:
            #Player 1 (turn value even)
            print(p1name, "yours turn")
            ans=input("What is on my mind?")
            if ans==picked_word:
                pp1=pp1+1
                print("Yours score is", pp1)
            else:
                print("Better luck next time, the word is", picked_word)
            c=int(input("Press 1 to continue and 0 to quit"))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        else:
            #Player 2(turn value odd)
            print(p2name, "yours turn")
            ans=input("What is on my mind?")
            if ans==picked_word:
                pp2=pp1+1
                print("Yours score is", pp1)
            else:
                print("Better luck next time, the word is", picked_word)
        c=int(input("Press 1 to continue and 0 to quit"))
        if c==0:
            thank(p1name,p2name,pp1,pp2)
            break
    turn=turn+1

play()
