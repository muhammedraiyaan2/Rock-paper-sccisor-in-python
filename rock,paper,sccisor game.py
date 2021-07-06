import random
#here I imported the random library
rand=random.randint(1,3)
#Here I told the computer to think 1 number to 3 number
inpu=input("Enter rock or paper or sccisor: ")
if(rand==1 and inpu=="sccisor" or rand==2 and inpu=="rock" or rand==3 and inpu=="paper"):
    print("Computer Won")
    #here add computer win function
elif(rand==1 and inpu=="paper" or rand==2 and inpu=="sccisor" or rand==3 and inpu=="rock"):
    print("user won")  
    #Here I add user win function  
else:
    print("draw")
    #here I add the draw function
if(rand==1):
    ad="rock"
elif(rand==2):
    ad="paper"
else:
    ad="sccisor"
print("Computer think number is ",rand,"is",ad)    