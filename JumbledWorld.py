import jumble as jumble

import  random





def choose():
    words = ['rainbow', 'computer', 'science', 'programming',
             'mathematics', 'player', 'condition', 'reverse',
             'water', 'board', 'geeks']
    return random.choice(words)


def jumble(word):
    random_world=random.sample(word,len(word))
    jumbled=''.join(random_world)
    return jumbled



def thank(p1n, p2n, p1, p2):
    print(p1n, 'Your score is :', p1)
    print(p2n, 'Your score is :', p2)

    # check_win() function calling
    check_win(p1n, p2n, p1, p2)

    print('Thanks for playing...')


def check_win(player1, player2, p1score, p2score):
    if p1score > p2score:
        print("winner is :", player1)
    elif p2score > p1score:
        print("winner is :", player2)
    else:
        print("Draw..Well Played guys..")


def play():
    p1name=input("Player 1 Enter your name")
    p2name=input("Player 2 Enter your name")

    pp1=0
    pp2=0

    turn=0

    while(1):
        pick_word=choose()
        qn=jumble(pick_word)
        print(qn)

        if(turn%2==0):
           print("player 1 turn")
           ans=input("What on your mind")
           if(ans==pick_word):
               pp1+=1
               print("Player 1 your score is",pp1)
           else:
               print("Better luck for next time")
           c=input("Press 1 continue 0 for exit")
           if(c==0):
               thank(p1name,p2name,pp1,pp2)
               break
           else:
               turn+=1
        else:
            print("player 2 turn")
            ans = input("What on your mind")
            if (ans == pick_word):
                pp2 += 1
                print("Player 2 your score is", pp2)
            else:
                print("Better luck for next time")
            c = input("Press 1 continue 0 for exit")
            if (c == 0):
                thank(p1name, p2name, pp1, pp2)
                break
            else:
                turn+=1



if __name__ == '__main__':
    # play() function calling
    play()