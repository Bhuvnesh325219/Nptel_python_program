
import string
from random import random

symbols=[]
symbols=list(string.ascii_letters)

card1=[0]*5
card2=[0]*5

print(card1)

pos1=random.randint(0,5)
pos2=random.randint(0,5)


samesymbols=random.choice(symbols)

symbols.remove(samesymbols)
if(pos1==pos2):
    card2[pos1]=samesymbols
    card1[pos1]=samesymbols
else:
    card1[pos1]=samesymbols
    card2[pos2] = samesymbols
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card1[pos1])



