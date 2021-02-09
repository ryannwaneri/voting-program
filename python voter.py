amount=int(input("please enter the amout of nominees:"))
nominees={}
choice=""

for x in range(amount):
    nomin=input("please enter nominee name:")
    nominees[nomin]=0
    
while not choice=="-1":
    choice=input("please enter your chosen candidate:")
    if not choice=="-1" and  choice in nominees.keys():
        nominees[choice]=nominees[choice]+1
    else:
        print("please enter a proper candidate")
        
for k,v in nominees.items():
    print(k+" has a total vote of "+str(v))