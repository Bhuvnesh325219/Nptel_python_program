





name1=list(input("Enter your name").lower())
name2=list(input("Enter your partner name").lower())


print(name1,"\n",name2)
#name1.sort()
#name2.sort()

for letter in name1[:]:
    if letter in name2:
        name1.remove(letter)
        name2.remove(letter)



count= len(name1)+len(name2)

flames=["Friends","Love","Affection","Marriage","Enemy","Siblings"]

i=0
current_count=0


while len(flames)>1:
    if current_count==count-1:
       flames.pop(i)
       current_count=0
    i = (i+1)%len(flames)
    current_count+=1


print(flames)




